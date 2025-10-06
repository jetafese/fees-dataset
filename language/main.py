import argparse
import os
import sys

from antlr4 import *
from bl.BLLexer import BLLexer
from bl.BLParser import BLParser
from smt import SMTCompiler, SMTConfig


# antlr4 -Dlanguage=Python3 BL.g4 -o bl -visitor
def main(input_file_name: str, config: SMTConfig):
    input_file = FileStream(input_file_name)
    lexer = BLLexer(input_file)
    stream = CommonTokenStream(lexer)
    parser = BLParser(stream)

    output_file_name, _ = os.path.splitext(input_file_name)
    output_file_name += ".smt2"

    with open(output_file_name, "w") as output_file:
        tree = parser.prog()
        output_file.write(SMTCompiler(config).generate_code(tree))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="BL to SMT compiler")
    parser.add_argument("-f", "--functions", action="store_true")
    parser.add_argument("input_file", type=str, help="Input BL file to be compiled")

    args = parser.parse_args()
    config = SMTConfig(
        use_functions=args.functions,
    )

    main(args.input_file, config)
