# Using the Checker

This is a short explanation walking through how to check the equivalence of natural-language- and BL-based formulations of fee calculations in SMT-LIB.

## Step 1: Generating Input Data

### From Natural Language

Use an LLM of choice (ChatGPT seems to work well) to generate data according to the prompt in `prompts/txt-smt.txt`, and save this data in a file.

### From BL

Use an LLM to generate BL code according to the prompt in `prompts/txt-bl.txt`. Then, run it through the BL to SMT compiler to obtain a `.smt2` file.

Ensure that any input and output variables have the same name across both programs.


## Step 2: Defining Background Assumptions
Depending on the nature of the input variables for the fee calculation, there may be additional conditions that are not encapsulated by the SMT descriptions of the calculation. As such, it may be necessary to specify bounds on one or more variables to ensure that the checker does not find spurious counterexamples (e.g. by assigning a negative value to a variable that cannot be negative in practice). This can be accomplished by creating a bounds file, which is a JSON file that takes the following format:

```
[
    {
        "variable": "weight",
        "min": 0,
        "max": 5
    },
    {
        "variable": "zone",
        "min": 1,
        "max": 15
    },
    ...
]
```

Note that the `min` and `max` fields are optional on each object.

## Step 3: Running the Checker

The checker can be run by using the command 

```
python3 checker.py bl.smt2 nl.smt2
```

where `bl.smt2` and `nl.smt2` contain the BL- and natural-language-based SMT formulations of the calculation. 

If bounds are also being specified, the command becomes

```
python3 checker.py bl.smt2 nl.smt2 bounds.json
```

where `bounds.json` is the bounds file.