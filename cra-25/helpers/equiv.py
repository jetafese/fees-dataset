import sys

from z3 import *

def check_equivalence(file1, file2):
    # Parse both SMT files
    with open(file1, "r") as f:
        smt1 = f.read()
    with open(file2, "r") as f:
        smt2 = f.read()

    # Convert to Z3 ASTs
    f1 = parse_smt2_string(smt1)
    f2 = parse_smt2_string(smt2)

    # Combine all assertions from both files
    assertions1 = And(f1)
    assertions2 = And(f2)

    s = Solver()

    # we check: NOT(assertions1 IFF assertions2)
    equiv_formula = (
        Or(And(assertions1, Not(assertions2)), And(assertions2, Not(assertions1)))
    )
    s.add(equiv_formula)

    if s.check() == unsat:
        print("✔️  The two SMT formulas are logically equivalent.")
    else:
        print("❌  The two SMT formulas are NOT equivalent.")
        print("Counterexample:")
        print(s.model())


# Example usage
if __name__ == "__main__":
    if len(sys.argv) > 4 or len(sys.argv) < 3:
        print("Usage: python equiv.py <file1.smt2> <file2.smt2>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    check_equivalence(file1, file2)
