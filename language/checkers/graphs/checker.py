import json
import re
import sys
import typing

from z3 import *

class VariableBounds(typing.TypedDict):
    type: typing.Literal["ranges", "equals", "outputs"]
    variables: list[str]
    min: float
    max: float


DECLARATION_REGEX = r"\(declare-const\s+(.+)\s+Real\)"


def extract_variables(smt2_string: str):
    """
    Extract real variables from an SMT-LIB string.

    This is difficult to do otherwise, because Z3 doesn't report don't-cares in its models.
    This means that we may not extract all variables if we were to obtain a model m and use
    decls() depending on the formulation we receive.

    See https://github.com/Z3Prover/z3/issues/1920
    """
    lines = smt2_string.split("\n")
    variables = set()

    for line in lines:
        match = re.match(DECLARATION_REGEX, line)

        if match is not None:
            variables.add(match.groups()[0])

    return variables


def extract_assumptions(bounds: list[VariableBounds], variables: set[str]):
    bound_assumptions_list = []
    output_assumptions_list = []

    for bound in bounds:
        if bound["type"] == "ranges":
            for variable_name in bound["variables"]:
                assert variable_name in variables, f"variable {variable_name} not found in SMT formulations"
                variable = z3.Real(variable_name)
                assert "min" in bound or "max" in bound, "range bounds must have min or max"
                if "min" in bound:
                    bound_assumptions_list.append(variable >= bound["min"])
                if "max" in bound:
                    bound_assumptions_list.append(variable <= bound["max"])

        elif bound["type"] == "equals":
            var_0 = bound["variables"][0]
            assert var_0 in variables, f"variable {var_0} not found in SMT formulations"
            z3_var_0 = z3.Real(var_0)
            for i in range(1, len(bound["variables"])):
                var_i = bound["variables"][i]
                assert var_i in variables, f"variable {var_i} not found in SMT formulations"
                z3_var_i = z3.Real(var_i)
                bound_assumptions_list.append(z3_var_0 == z3_var_i)

        elif bound["type"] == "outputs":
            out_0 = bound["variables"][0]
            assert out_0 in variables, f"variable {out_0} not found in SMT formulations"
            z3_out_0 = z3.Real(out_0)
            for i in range(1, len(bound["variables"])):
                out_i = bound["variables"][i]
                assert out_i in variables, f"variable {out_i} not found in SMT formulations"
                z3_out_i = z3.Real(out_i)
                output_assumptions_list.append(z3_out_0 == z3_out_i)
        else:
            assert False, f"unknown bound type {bound['type']}"

    return And(bound_assumptions_list), And(output_assumptions_list)


def check_equivalence(file1, file2, bounds_file):
    # Parse both SMT files
    with open(file1, "r") as f:
        smt1 = f.read()
    with open(file2, "r") as f:
        smt2 = f.read()

    variables = extract_variables(smt1).union(extract_variables(smt2))

    if bounds_file is None:
        bound_assumptions = And()
        output_assumptions = And()
    else:
        with open(bounds_file, "r") as f:
            bounds: list[VariableBounds] = json.load(f)

        bound_assumptions, output_assumptions = extract_assumptions(bounds, variables)

    # Convert to Z3 ASTs
    f1 = parse_smt2_string(smt1)
    f2 = parse_smt2_string(smt2)

    # Combine all assertions from both files
    assertions1 = And(f1)
    assertions2 = And(f2)

    background_assumptions = bound_assumptions
    s = Solver()

    ## assume that we have all assumption in background variable D
    ## further assume, both files have 'weight' and fee_nl, fee_bl
    # we check: (assertions1 ^ assertions2 ^ D => fee_nl = fee_bl)
    equiv_formula = (
        And(assertions1, assertions2, background_assumptions, Not(output_assumptions)),
    )
    s.add(equiv_formula)

    # alternatively, if we have fee as the output variable in both input files,
    # we want D => ((A ^ B) v (!A ^ !B)) (i.e. D => (A <=> B)) to hold
    # equiv_formula = Or(
    #     And(assertions1, assertions2), And(Not(assertions1), Not(assertions2))
    # )
    # # we want to see if it is possible to have the background conditions not being sufficient for equivalence
    # s.add(background_assumptions)
    # s.add(Not(equiv_formula))

    if s.check() == unsat:
        print("✔️  The two SMT formulas are logically equivalent.")
    else:
        print("❌  The two SMT formulas are NOT equivalent.")
        print("Counterexample:")
        print(s.model())


# Example usage
if __name__ == "__main__":
    if len(sys.argv) > 4 or len(sys.argv) < 3:
        print("Usage: python checker.py <file1.smt2> <file2.smt2> <bounds.json>?")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    bounds_file = sys.argv[3] if len(sys.argv) == 4 else None
    check_equivalence(file1, file2, bounds_file)
