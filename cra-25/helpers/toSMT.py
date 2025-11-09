import json
import sys
import re

def extract_variables(expr):
    """
    Extract variable names from an SMT expression.
    Assumes variables are alphanumeric and underscores, not numbers or SMT operators.
    """
    # Match sequences of letters, numbers, and underscores starting with a letter/underscore
    tokens = re.findall(r"[A-Za-z_][A-Za-z0-9_]*", expr)
    # Exclude common SMT-LIB keywords/operators
    keywords = {"ite", "and", "or", "not", "=", "+", "-", "*", "/", ">", "<", ">=", "<=", "=>"}
    return [t for t in tokens if t not in keywords]

def collect_variables(translations):
    vars_set = set()
    for item in translations:
        if "if" in item:
            for cond in item["if"]:
                vars_set.update(extract_variables(cond["smtExpr"]))
        if "then" in item:
            for t in item["then"]:
                vars_set.update(extract_variables(t["smtExpr"]))
        if "smtExpr" in item:
            vars_set.update(extract_variables(item["smtExpr"]))
    return vars_set

def json_to_smtlib(json_file, smt_file):
    """
    Convert a JSON translations file into SMT-LIB format.
    """
    with open(json_file) as f:
        data = json.load(f)

    smtlib_lines = []
    translations = data.get("translations", [])

    # Automatically detect variables
    variables = collect_variables(translations)
    for var in sorted(variables):
        smtlib_lines.append(f"(declare-const {var} Real)")
    smtlib_lines.append("")  # blank line

    # Process translations
    for item in translations:
        if "if" in item and "then" in item:
            # Combine conditions
            if_exprs = [cond["smtExpr"] for cond in item["if"]]
            combined_if = "(and " + " ".join(if_exprs) + ")" if len(if_exprs) > 1 else if_exprs[0]

            # Combine then clauses
            then_exprs = [t["smtExpr"] for t in item["then"]]
            combined_then = "(and " + " ".join(then_exprs) + ")" if len(then_exprs) > 1 else then_exprs[0]

            smtlib_lines.append(f"(assert (=> {combined_if} {combined_then}))")
        elif "smtExpr" in item:
            smtlib_lines.append(f"(assert {item['smtExpr']})")

    # Write SMT-LIB file
    with open(smt_file, "w") as f:
        f.write("\n".join(smtlib_lines))

    print(f"SMT-LIB file '{smt_file}' generated!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python toSMT.py <input.json> <output.smt2>")
        sys.exit(1)

    json_file = sys.argv[1]
    smt_file = sys.argv[2]

    json_to_smtlib(json_file, smt_file)
