import json
import re
import sys
import typing
import warnings

from z3 import *


class VariableBounds(typing.TypedDict):
    type: typing.Literal["equals", "outputs", "ranges"]
    variables: list[str]
    min: typing.NotRequired[float]
    max: typing.NotRequired[float]


DECLARATION_REGEX = r"\(declare-const\s+(.+?)\s+Real\)"  # +? is non-greedy


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

    for match in re.finditer(DECLARATION_REGEX, smt2_string):
        if match is not None:
            variables.add(match.groups()[0])

    return variables


def extract_assumptions(
    bounds: list[VariableBounds], variables1: set[str], variables2: set[str]
):
    bound_assumptions_list = []
    output_assumptions_list = []

    inter_program_bounds = False

    for bound in bounds:
        for variable_name in bound["variables"]:
            assert (
                variable_name in variables1 or variable_name in variables2
            ), f"variable {variable_name} not found in SMT formulations"
            variable = z3.Real(variable_name)

    for bound in bounds:
        if bound["type"] == "ranges":
            if "min" in bound:
                bound_assumptions_list.append(variable >= bound["min"])
            if "max" in bound:
                bound_assumptions_list.append(variable <= bound["max"])

        elif bound["type"] == "equals":
            variable_0 = z3.Real(bound["variables"][0])
            contains_from_v1 = bound["variables"][0] in variables1
            contains_from_v2 = bound["variables"][0] in variables2

            for i in range(1, len(bound["variables"])):
                variable_i = z3.Real(bound["variables"][i])
                bound_assumptions_list.append(variable_0 == variable_i)
                contains_from_v1 = (
                    contains_from_v1 or bound["variables"][i] in variables1
                )
                contains_from_v2 = (
                    contains_from_v2 or bound["variables"][i] in variables2
                )

            if contains_from_v1 and contains_from_v2:
                inter_program_bounds = True

        elif bound["type"] == "outputs":
            variable_0 = z3.Real(bound["variables"][0])

            for i in range(1, len(bound["variables"])):
                variable_i = z3.Real(bound["variables"][i])
                output_assumptions_list.append(variable_0 == variable_i)

        else:
            assert False, f"unknown bound type {bound['type']}"

    if not inter_program_bounds:
        warnings.warn(
            f"No equality bounds specified between variables in the two programs, only variables shared are {variables1.intersection(variables2)}"
        )
    if len(output_assumptions_list) == 0:
        warnings.warn(f"No assertions provided on program output")

    return And(bound_assumptions_list), And(output_assumptions_list)


def check_equivalence(file1, file2, bounds_file):
    # Parse both SMT files
    with open(file1, "r") as f:
        smt1 = f.read()
    with open(file2, "r") as f:
        smt2 = f.read()

    f1_variables = extract_variables(smt1)
    f2_variables = extract_variables(smt2)

    if bounds_file is None:
        bound_assumptions = And()
        output_assumptions = And()
    else:
        with open(bounds_file, "r") as f:
            bounds: list[VariableBounds] = json.load(f)

        bound_assumptions, output_assumptions = extract_assumptions(
            bounds, f1_variables, f2_variables
        )

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
