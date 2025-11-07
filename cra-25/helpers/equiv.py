import sys

from z3 import *

def check_equivalence(file1, file2, file3=None):
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

    if file3 is None:
        # we check: NOT(assertions1 IFF assertions2)
        equiv_formula = Or(
            And(assertions1, Not(assertions2)), And(assertions2, Not(assertions1))
        )
        s.add(equiv_formula)

        if s.check() == unsat:
            print("✔️  The two SMT formulas are logically equivalent.")
        else:
            print("❌  The two SMT formulas are NOT equivalent.")
            print("Counterexample:")
            print(s.model())
    else:
        with open(file3, "r") as f:
            smt3 = f.read()
        f3 = parse_smt2_string(smt3)
        assertions3 = And(f3)
        # we check: (assertions1 IFF assertions2),
        # (assertions2 IFF assertions3), (assertions1 IFF assertions3)
        e1 = None; e2 = None; e3 = None # flags to check equivalence
        equiv_formula_1 = Or(
            And(assertions1, Not(assertions2)), And(assertions2, Not(assertions1))
        )
        s.push()
        s.add(equiv_formula_1)
        if s.check() != unsat:
            e1 = s.model()
        s.pop()
        equiv_formula_2 = Or(
            And(assertions2, Not(assertions3)), And(assertions3, Not(assertions2))
        )
        s.push()
        s.add(equiv_formula_2)
        if s.check() != unsat:
            e2 = s.model()
        s.pop()
        equiv_formula_3 = Or(
            And(assertions1, Not(assertions3)), And(assertions3, Not(assertions1))
        )
        s.push()
        s.add(equiv_formula_3)
        if s.check() != unsat:
            e3 = s.model()
        s.pop()

        if e1 is not None and e2 is not None and e3 is not None:
            # The three SMT formulas are not logically equivalent;
            # pick file2 as representative counterexample
            print(e2)
        else:
            # There exists a pair of equivalent SMT formulas (2/3)
            if e1 is None:
                print(smt1)
            elif e2 is None:
                print(smt2)
            elif e3 is None:
                print(smt3)

# Example usage
if __name__ == "__main__":
    if len(sys.argv) > 4 or len(sys.argv) < 3:
        print("Usage: python equiv.py <file1.smt2> <file2.smt2>")
        sys.exit(1)

    file1 = sys.argv[1]
    file2 = sys.argv[2]
    if len(sys.argv) == 4:
        file3 = sys.argv[3]
        check_equivalence(file1, file2, file3)
    else:
        check_equivalence(file1, file2)