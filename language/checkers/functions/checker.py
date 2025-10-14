import json
import sys
import typing

from z3 import *


class FunctionBounds(typing.TypedDict):
    type: typing.Literal["strict", "mapping"]
    functions: list[str]
    mapping: list[int]


def extract_assertions(bounds: list[FunctionBounds], model: dict[str, typing.Any]):
    output_assertions = []
    for bound in bounds:
        if len(bound["functions"]) < 2:
            raise AssertionError("Must assert equivalence between at least 2 functions")

        # this doesn't assume that there are only 2 functions to compare
        f_0 = model[bound["functions"][0]]

        for i in range(1, len(bound["functions"])):
            f_i = model[bound["functions"][i]]
            n = f_0.arity()

            # xs = [Real(f"x{j}") for j in range(n)]
            xs = Array("xs", IntSort(), RealSort())

            if bound["type"] == "strict":
                assert n == f_i.arity(), "Functions must have same arity"
                output_assertions.append(
                    ForAll(
                        [xs],
                        f_0(*[xs[j] for j in range(f_0.arity())])
                        == f_i(*[xs[j] for j in range(f_i.arity())]),
                    )
                )

            elif bound["type"] == "mapping":
                # introduce a symbolic mapping as a finite vector of ints
                mapping = [Int(f"m{j}") for j in range(f_i.arity())]
                constraints = [
                    And(0 <= mapping[j], mapping[j] < n) for j in range(f_i.arity())
                ]
                # mapping equality condition
                condition = ForAll(
                    [xs],
                    f_0(*[xs[j] for j in range(f_0.arity())])
                    == f_i(*[xs[mapping[j]] for j in range(f_i.arity())]),
                )
                output_assertions.append(
                    Exists(mapping, And(constraints + [condition]))
                )

            else:
                raise AssertionError(f"Unknown bound type {bound['type']}")

    return And(output_assertions)


def check_equivalence(file1: str, file2: str, bounds_file: str | None = None):
    s = Solver()

    for file in file1, file2:
        ast = parse_smt2_file(file)
        s.add(And(ast))

    # refer to checker/functions/README.md for more information
    assert s.check() == z3.sat, "Model is not satisfiable"
    model_vars = {item.name(): item for item in s.model()}

    if bounds_file is None:
        output_assertions = And()
    else:
        with open(bounds_file, "r") as f:
            bounds: list[FunctionBounds] = json.load(f)

        output_assertions = extract_assertions(bounds, model_vars)

    s.add(Not(output_assertions))

    if s.check() == unsat:
        print("✔️  The two SMT formulas are logically equivalent.")
    else:
        print("❌  The two SMT formulas are NOT equivalent.")
        print("Counterexample:")
        print(s.model())


if __name__ == "__main__":
    if len(sys.argv) > 4 or len(sys.argv) < 3:
        print("Usage: python checker.py <file1.smt2> <file2.smt2> <bounds.json>?")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    bounds_file = sys.argv[3] if len(sys.argv) == 4 else None
    check_equivalence(file1, file2, bounds_file)
