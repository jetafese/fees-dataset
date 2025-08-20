import os
import csv
import argparse

def process_csv(csv_file):
    # Check if the file exists
    if not os.path.exists(csv_file):
        print(f"Error: The file {csv_file} does not exist.")
        return

    # Read the CSV file
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        # Loop through each row in the CSV
        for row in reader:
            # Extract the values
            fee_type = row['type']
            currency = row['currency']
            condition = row['condition']
            formula = row['formula']

            # Create the directory path
            directory = os.path.join(fee_type, currency, condition)
            os.makedirs(directory, exist_ok=True)

            # Create the path to the formula.txt file
            formula_file = os.path.join(directory, 'formula.txt')

            # Write the formula to the formula.txt file
            with open(formula_file, mode='w', encoding='utf-8') as formula_f:
                formula_f.write(formula)

            print(f"Created: {formula_file}")

def main():
    # Set up command-line argument parsing
    parser = argparse.ArgumentParser(description="Process a CSV file containing PayPal fees")
    parser.add_argument('csv_file', help="Path to the CSV file to process")

    # Parse the command-line arguments
    args = parser.parse_args()

    # Process the CSV file
    process_csv(args.csv_file)

if __name__ == "__main__":
    main()

