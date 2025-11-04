import argparse
import csv
import os


# Headers:
# 	       Single Filer		Married Filing Jointly		Standard Deduction		    Personal Exemption
# State	 Rates Brackets	        Rates	Brackets	   Single	Couple	Single	    Couple	Dependent
def parse_tax_csv(csv_file):
    """Parse the CSV and group rows by state, collecting single/joint brackets."""
    with open(csv_file, newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        rows = list(reader)

    # Filter out completely empty lines
    rows = [r for r in rows if any(cell.strip() for cell in r)]

    states = {}
    current_state = None

    for row in rows:
        if not row or not any(row):
            continue
        state = row[0].strip()
        single_rate = row[1].strip() if len(row) > 1 else ""
        single_bracket = row[3].strip() if len(row) > 3 else ""
        joint_rate = row[4].strip() if len(row) > 4 else ""
        joint_bracket = row[6].strip() if len(row) > 6 else ""

        # new state row
        if state:
            current_state = state
            states[current_state] = {"single": [], "joint": []}

        # Skip states with "none" for both
        if single_rate.lower() == "none" and joint_rate.lower() == "none":
            states.pop(current_state, None)
            current_state = None
            continue

        if not current_state:
            continue

        # Collect valid data
        if single_rate and single_rate.lower() != "none":
            states[current_state]["single"].append((single_rate, single_bracket))
        if joint_rate and joint_rate.lower() != "none":
            states[current_state]["joint"].append((joint_rate, joint_bracket))
    return states


def write_tax_files(states, base_dir="output"):
    """Generate directory and file structure with formatted text."""
    os.makedirs(base_dir, exist_ok=True)

    for state, brackets in states.items():
        state_dir = os.path.join(base_dir, state.lower())
        os.makedirs(state_dir, exist_ok=True)

        for filing_status, entries in brackets.items():
            if not entries:
                continue

            sub_dir = os.path.join(state_dir, filing_status)
            os.makedirs(sub_dir, exist_ok=True)
            file_path = os.path.join(sub_dir, f"{state.lower()}.txt")

            # Clean up currency symbols and whitespace
            def clean(val):
                return val.replace("$", "").replace(",", "").strip()

            with open(file_path, "w", encoding="utf-8") as f:
                f.write("Tax rate,Taxable income threshold\n")
                for i, (rate, threshold) in enumerate(entries):
                    threshold_clean = clean(threshold or "$0")

                    if i == 0 and len(entries) > 1:
                        next_thresh = clean(entries[i+1][1]) if len(entries) > 1 else threshold_clean
                        line = f"{rate}, on the portion of taxable income that is ${next_thresh} or less, plus\n"
                    elif i < len(entries) - 1:
                        next_thresh = clean(entries[i+1][1])
                        line = f"{rate}, on the portion of taxable income over ${threshold_clean} up to ${next_thresh} plus\n"
                    else:
                        line = f"{rate}, on the portion of taxable income over ${threshold_clean}\n"

                    f.write(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Generate tax bracket files by state from a CSV."
    )
    parser.add_argument(
        "csv_file",
        help="Path to the tax data CSV file (e.g., tax_data.csv)"
    )
    parser.add_argument(
        "-o", "--output",
        default="output",
        help="Directory to store generated files (default: ./output)"
    )
    args = parser.parse_args()

    states = parse_tax_csv(args.csv_file)
    write_tax_files(states, args.output)
    print(f"✅ Tax files generated in: {os.path.abspath(args.output)}")
