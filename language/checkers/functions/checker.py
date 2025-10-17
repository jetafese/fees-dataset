from dataclasses import dataclass, field
import json
import sys
import typing

from z3 import *

MAX_CONDITIONS = 100


class FunctionBounds(typing.TypedDict):
    type: typing.Literal["strict", "mapping"]
    functions: list[str]
    mapping: list[list[str]]
    inputs: str


@dataclass
class ParamFunction:
    decl: FuncDeclRef
    params: list[str]


@dataclass
class AssertionData:
    bound_assumptions: BoolRef = And()
    output_assertions: BoolRef = And()
    # keep track of the number of elements we reference in a given input array
    input_arrays: list[tuple[ArrayRef, int]] = field(default_factory=[])


def parse_functions(file: str) -> dict[str, ParamFunction]:
    functions: dict[str, ParamFunction] = {}
    ast = parse_smt2_file(file)

    for expr in ast:
        if is_quantifier(expr):
            num_vars = expr.num_vars()
            var_names = [expr.var_name(i) for i in range(num_vars)]
        body = expr.body()
        if is_eq(body):
            lhs = body.arg(0)
            if is_app(lhs):
                decl = lhs.decl()
                func_name = lhs.decl().name()
                functions[func_name] = ParamFunction(decl=decl, params=var_names)

    return functions


def extract_assertions(
    bounds: list[FunctionBounds], functions: dict[str, ParamFunction]
):
    bound_assumptions = []
    output_assertions = []
    input_arrays = []
    for bound in bounds:
        if len(bound["functions"]) < 2:
            raise AssertionError("Must assert equivalence between at least 2 functions")

        # this doesn't assume that there are only 2 functions to compare
        f_0 = functions[bound["functions"][0]].decl

        for i in range(1, len(bound["functions"])):
            f_i = functions[bound["functions"][i]].decl

            xs = Array(bound["inputs"], IntSort(), RealSort())

            if bound["type"] == "strict":
                assert f_0.arity() == f_i.arity(), "Functions must have same arity"
                output_assertions.append(
                    f_0(*[xs[j] for j in range(f_0.arity())])
                    == f_i(*[xs[j] for j in range(f_i.arity())]),
                )

                input_arrays.append((xs, f_0.arity()))

            elif bound["type"] == "mapping":
                mapped_functions = [functions[f] for f in bound["functions"]]
                index_mappings: list[list[int]] = [
                    list(range(f.decl.arity())) for f in mapped_functions
                ]
                for param_mapping in bound["mapping"]:
                    assert len(param_mapping) == len(mapped_functions)

                    # find position in the first function's params list to map to
                    original_param_index = mapped_functions[0].params.index(
                        param_mapping[0]
                    )

                    for i in range(1, len(param_mapping)):
                        # find position in the current function's param list to map to
                        current_param_index = mapped_functions[i].params.index(
                            param_mapping[i]
                        )
                        index_mappings[i][current_param_index] = original_param_index

                xs = Array(bound["inputs"], IntSort(), RealSort())
                f_0 = mapped_functions[0].decl

                for f_i, mapping in zip(mapped_functions[1:], index_mappings[1:]):
                    f_i = f_i.decl
                    output_assertions.append(
                        f_0(*[xs[j] for j in range(f_0.arity())])
                        == f_i(*[xs[mapping[j]] for j in range(f_i.arity())])
                    )

                input_arrays.append((xs, max(f.decl.arity() for f in mapped_functions)))

            else:
                raise AssertionError(f"Unknown bound type {bound['type']}")

    return AssertionData(
        bound_assumptions=And(bound_assumptions),
        output_assertions=And(output_assertions),
        input_arrays=input_arrays,
    )


def check_equivalence(file1: str, file2: str, bounds_file: str | None = None):
    s = Solver()

    functions: dict[str, ParamFunction] = {}

    # extract functions and constraints from input files
    for file in file1, file2:
        functions |= parse_functions(file)
        ast = parse_smt2_file(file)
        s.add(And(ast))

    # refer to checker/functions/README.md for more information
    assert s.check() == z3.sat, "Model is not satisfiable"

    if bounds_file is None:
        assertion_data = AssertionData()
    else:
        with open(bounds_file, "r") as f:
            bounds: list[FunctionBounds] = json.load(f)

        assertion_data = extract_assertions(bounds, functions)

    s.add(assertion_data.bound_assumptions)
    s.add(Not(assertion_data.output_assertions))

    conditions = []
    counterexample = None
    while s.check() == sat and len(conditions) < MAX_CONDITIONS:
        model = s.model()
        for ary, length in assertion_data.input_arrays:
            condition = And(*[ary[i] != model.evaluate(ary[i]) for i in range(length)])
            s.add(condition)
            conditions.append(condition)

            if counterexample is None:
                counterexample = f"{ary.decl().name()}: {[model.evaluate(ary[i]) for i in range(length)]}"

    if s.check() == unsat:
        print(
            "✔️  The two SMT formulas are logically equivalent, modulo the following conditions:"
        )

        for condition in conditions:
            print(condition)
    else:
        print("❌  The two SMT formulas are NOT equivalent.")
        print("Counterexample:")
        print(counterexample)


if __name__ == "__main__":
    if len(sys.argv) > 4 or len(sys.argv) < 3:
        print("Usage: python checker.py <file1.smt2> <file2.smt2> <bounds.json>?")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    bounds_file = sys.argv[3] if len(sys.argv) == 4 else None
    check_equivalence(file1, file2, bounds_file)
