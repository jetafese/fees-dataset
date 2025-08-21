# PayPal Fees Dataset

This repository contains a dataset in CSV format that includes PayPal fees for both merchants and consumers. The fees are sourced from PayPal's official documentation for business (merchant) and consumer fees. This dataset is useful for understanding the various fee structures for different types of transactions through PayPal.

## Table of Contents

- [About the Dataset](#about-the-dataset)
- [CSV Structure](#csv-structure)
- [Sources](#sources)
- [Usage](#usage)
- [License](#license)

## About the Dataset

The dataset includes the following fee categories as of August 20, 2025:

- **Merchant Fees**: Fees associated with businesses accepting PayPal payments.
- **Consumer Fees**: Fees for consumers when sending money or making payments through PayPal.

Each row in the dataset represents a unique PayPal fee based on the transaction type, the currency, and the conditions under which the fee applies. The dataset includes both percentage-based and fixed fees, as well as conditional logic for different transaction amounts or situations.

## CSV Structure

The CSV file contains the following columns:

- **type**: The type of fee (e.g., `consumer-crypto`, `consumer-donations`).
- **kind**: Defines whether the fee is for consumers or merchants.
- **currency**: The currency in which the fee applies (e.g., USD, AUD, BRL).
- **condition**: The condition under which the fee applies (e.g., `range`, `Donate-Button`).
- **formula**: Describes how the fee is calculated (e.g., percentage, fixed amount, or combination).

### Example Entries:

| type               | kind     | currency | condition         | formula                                      |
|--------------------|----------|----------|-------------------|----------------------------------------------|
| consumer-crypto    | consumer | USD      | range             | if amount is between 1.00 - 74.99 USD, then 2.2% |
| consumer-crypto    | consumer | USD      | range             | if amount is between 75.00 – 200.00 USD, then 2% |
| consumer-crypto    | consumer | USD      | range             | if amount is between 200.01 – 1000.00 USD, then 1.8% |
| consumer-crypto    | consumer | USD      | range             | if amount is > 1000.01 USD, then 1.5%       |
| consumer-donations | consumer | AUD      | Donate-Button     | 2.89% + 0.59 AUD                            |
| consumer-donations | consumer | BRL      | Donate-Button     | 2.89% + 2.90 BRL                            |
| consumer-donations | consumer | CAD      | Donate-Button     | 2.89% + 0.59 CAD                            |
| consumer-donations | consumer | CZK      | Donate-Button     | 2.89% + 9.00 CZK                            |

### Types of Fees:
- **Consumer Fees**: Fees for consumers when sending money or making payments.
- **Merchant Fees**: Fees for businesses accepting PayPal payments.

### Common Fee Conditions:
- **range**: A percentage fee based on the transaction amount range.
- **Donate-Button**: A specific fee applied to donations through a PayPal button.

## Sources

- **Merchant Fees**: [PayPal Merchant Fees](https://www.paypal.com/us/business/paypal-business-fees)
- **Consumer Fees**: [PayPal Consumer Fees](https://www.paypal.com/us/digital-wallet/paypal-consumer-fees)

These links contain the official details regarding the current fee structures for both merchants and consumers.

## Usage

To use the dataset:

1. Download the CSV file.
2. Open it in any CSV-compatible program (e.g., Microsoft Excel, Google Sheets, or a text editor).
3. You can analyze the data by filtering, sorting, or using it for any business or financial analysis.

## License

This dataset is provided under the [MIT License](LICENSE). Feel free to use, modify, or distribute the data as per your needs.

## Contributions

Contributions are welcome! If you find any errors or have suggestions for improving the dataset, please submit an issue or a pull request.

