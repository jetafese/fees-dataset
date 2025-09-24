import sys

from z3 import *


def check_equivalence(file1, file2):
    # Parse both SMT files
    with open(file1, 'r') as f:
        smt1 = f.read()
    with open(file2, 'r') as f:
        smt2 = f.read()

    # Convert to Z3 ASTs
    f1 = parse_smt2_string(smt1)
    f2 = parse_smt2_string(smt2)
    # variables1 = { d.decl().name(): d for d in f1 }
    # print(f1[0].assertion())

    # Combine all assertions from both files
    assertions1 = And(f1)
    assertions2 = And(f2)

    ## assume that we have all assumption in background variable D
    ## further assume, both files have 'weight' and fee_nl, fee_bl
    # we check: (assertions1 ^ assertions2 ^ D => fee_nl = fee_bl)
    # equiv_formula = And(And(assertions1, assertions2, D), And(Not(fee_nl = fee_bl)))

    # Now check (A ∧ ¬B) ∨ (¬A ∧ B)
    s = Solver()
    equiv_formula = Or(And(assertions1, Not(assertions2)),
                       And(Not(assertions1), assertions2))
    s.add(equiv_formula)

    if s.check() == unsat:
        print("✔️  The two SMT formulas are logically equivalent.")
    else:
        print("❌  The two SMT formulas are NOT equivalent.")
        print("Counterexample:")
        print(s.model())

# Example usage
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python checker.py <file1.smt2> <file2.smt2>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    check_equivalence(file1, file2)
