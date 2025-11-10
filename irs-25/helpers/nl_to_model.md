<role>
You are a helpful logicial who extracts logical variables from natural language according to a given schema.
</role>

<instructions>
1. Write a json file that captures variable definitions and their descriptions using the following schema:
<schema>
{
  "types": [],
  "variables": [
    {
        "name" : "Income",
        "type" : "NUMBER",
        "description" : "Income amount for tax purposes"
    },
    {
      "name": "Bracket_i",
      "type": "NUMBER",
      "description": "Taxes for Bracket i. Always included in the sum; 0 if income does not reach this bracket."
    },
    {
      "name": "FinalTaxes",
      "type": "NUMBER",
      "description": "Sum of all Bracket_i in numerical order. Includes zeros from brackets that do not apply. Calculation must always add all i brackets explicitly."
    }
  ],
  "rules": [
    {
      "id": "DFV12ES58TNM",
      "expression": "(>= FinalTaxes 0)",
      "translation": "FinalTaxes is greater or equal to 0"
    }]
}
</schema>
</instructions>

<example>
<input>
<description>
Alberta income tax rates for 2025
Tax rate	Taxable income threshold
8%	on the portion of taxable income that is $60,000 or less, plus
10%	on the portion of taxable income over $60,000 up to $151,234, plus
12%	on the portion of taxable income over $151,234 up to $181,481, plus
13%	on the portion of taxable income over $181,481 up to $241,974, plus
14%	on the portion of taxable income over $241,974 up to $362,961, plus
15%	on the portion of taxable income over $362,961
</description>
</input>

<output>
{
  "types": [],
  "variables": [
    {
      "name": "Income",
      "type": "NUMBER",
      "description": "Total taxable income for Alberta 2025 tax calculation."
    },
    {
      "name": "Bracket_1",
      "type": "NUMBER",
      "description": "Taxes for Bracket 1: 8% on the portion of income up to $60,000. Always included in the sum; 0 if income does not reach this bracket."
    },
    {
      "name": "Bracket_2",
      "type": "NUMBER",
      "description": "Taxes for Bracket 2: 10% on the portion of income over $60,000 up to $151,234. Always included in the sum; 0 if income does not reach this bracket."
    },
    {
      "name": "Bracket_3",
      "type": "NUMBER",
      "description": "Taxes for Bracket 3: 12% on the portion of income over $151,234 up to $181,481. Always included in the sum; 0 if income does not reach this bracket."
    },
    {
      "name": "Bracket_4",
      "type": "NUMBER",
      "description": "Taxes for Bracket 4: 13% on the portion of income over $181,481 up to $241,974. Always included in the sum; 0 if income does not reach this bracket."
    },
    {
      "name": "Bracket_5",
      "type": "NUMBER",
      "description": "Taxes for Bracket 5: 14% on the portion of income over $241,974 up to $362,961. Always included in the sum; 0 if income does not reach this bracket."
    },
    {
      "name": "Bracket_6",
      "type": "NUMBER",
      "description": "Taxes for Bracket 6: 15% on the portion of income above $362,961. Always included in the sum; 0 if income does not reach this bracket."
    },
    {
      "name": "FinalTaxes",
      "type": "NUMBER",
      "description": "Sum of Bracket_1 through Bracket_6 in numerical order. Includes zeros from brackets that do not apply. Calculation must always add all six brackets explicitly."
    }
  ],
  "rules": [
    {
      "id": "DFV12ES58TNM",
      "expression": "(>= FinalTaxes 0)",
      "translation": "FinalTaxes is greater or equal to 0"
    }]
}
</output>
</example>

Now you generate the output for the following input. Please ensure to also have
<output> tags in your final response.
<input>
<description>
${description}
</description>
</input>
