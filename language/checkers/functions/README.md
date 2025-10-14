# Using the Checker

This is a short explanation walking through how to check the equivalence of natural-language- and BL-based formulations of fee calculations in SMT-LIB.

## Step 1: Generating Input Data

### From Natural Language

Use an LLM of choice (ChatGPT seems to work well) to generate data according to the prompt in `prompts/txt-smt.txt`, and save this data in a file.

### From BL

Use an LLM to generate BL code according to the prompt in `prompts/txt-bl.txt`. Then, run it through the BL to SMT compiler to obtain a `.smt2` file and a `-f` option so that functions are generated instead of the graph representation.

Ensure that any input and output variables have the same name across both programs.


## Step 2: Defining Background Assumptions
Depending on the nature of the input variables for the fee calculation, there may be additional conditions that are not encapsulated by the SMT descriptions of the calculation. As such, it may be necessary to specify bounds on one or more variables to ensure that the checker does not find spurious counterexamples (e.g. by assigning a negative value to a variable that cannot be negative in practice). This can be accomplished by creating a bounds file, which is a JSON file that takes the following format:

```
[
    {
        "type": "ranges",
        "variables": ["weigh"],
        "min": 0,
        "max": 5
    },
    {
        "type": "outputs",
        "variables": ["fee_nl", "fee_bl"]
    },
    {
        "type": "equals",
        "variables": ["weight", "weigh"]
    },
    ...
]
```

There are currently three types of constraint supported in these files:

- the `range` type lets us specify a numeric range on the values of a set of variables (`min` and `max` are optional)
- the `equals` type lets us specify that a set of variables are all equal to each other
- the `outputs` type lets us specify the output variables (which should all be equal to each other if the formulas are equivalent)


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

### A note about the checker

The checker makes the following assumptions:
1. Each file ensures that the functions are placed in `(assert ...)` blocks. This is an artifact of history that makes it easier to extract the function names from a Z3 model.
2. The functions are satisfiable so that a model can be extracted.