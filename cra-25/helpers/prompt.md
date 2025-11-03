The government of canada has specified the taxes for the 2025 year at the
following site: https://www.canada.ca/en/revenue-agency/services/tax/individuals/frequently-asked-questions-individuals/canadian-income-tax-rates-individuals-current-previous-years.html

We are going to translate the files (e.g., federal.txt) to SMT and also request
an LLM generate programs in BL (see grammar in language/BL.g4). These programs
can take private variables such as SIN into account to simulate reality. For
example, temporary foreign workers have SINs that start with 9 (e.g. 900999999)
where they would be exempt from paying taxes under certain schemes.

See cra-25/mappings for examples on the bounds file usage and how the checker would work.
