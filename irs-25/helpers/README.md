## IRS-25

This folder introduces the specs for the IRS across single and married filing
jointly categories for the federal government and states that charge income tax.

Federal taxes for the 2025 year: https://www.irs.gov/filing/federal-income-tax-rates-and-brackets
State taxes for the 2025 year: https://taxfoundation.org/data/all/state/state-income-tax-rates/

## Structure

```
├── alabama
│   ├── joint
│   │   └── alabama.txt         (state taxes for married filing jointly)
│   └── single
│       └── alabama.txt         (state taxes for single filers)
├── arizona
│   ├── joint
│   │   └── arizona.txt
│   └── single
│       └── arizona.txt
...
├── helpers
│   ├── 2025-State-Individual-Income-Tax-Rates-and-Brackets-2025.xlsx
│   ├── create_jobs.py          (script to generate directory structure of jobs)
│   ├── jobs.csv                (csv version of 2025 data set)
│   ├── model.json              (specifying key variables for LLM use)
│   ├── nl_to_bl.md             (prompt for generating BL code from jobs)
│   └── README.md               (this file)
...
├── west-virginia
│   ├── joint
│   │   └── west-virginia.txt
│   └── single
│       └── west-virginia.txt
└── wisconsin
    ├── joint
    │   └── wisconsin.txt
    └── single
        └── wisconsin.txt
```


## Workflow
See the example in cra-25/helpers/example for details and workflow.
