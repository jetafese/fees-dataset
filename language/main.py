import os
import sys

from antlr4 import *
from bl.BLLexer import BLLexer
from bl.BLParser import BLParser
from smt import SMTCompiler, SMTConfig


# antlr4 -Dlanguage=Python3 BL.g4 -o bl -visitor
def main(argv):
    input_file = FileStream(argv[1])
    lexer = BLLexer(input_file)
    stream = CommonTokenStream(lexer)
    parser = BLParser(stream)

    output_file_name, _ = os.path.splitext(argv[1])
    output_file_name += ".smt2"

    with open(output_file_name, "w") as output_file:
        tree = parser.prog()
        output_file.write(
            SMTCompiler(SMTConfig(use_functions=True)).generate_code(tree)
        )


if __name__ == "__main__":
    main(sys.argv)
