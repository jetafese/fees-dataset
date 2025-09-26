import sys

from antlr4 import *
from bl.BLLexer import BLLexer
from bl.BLParser import BLParser
from smt import generate_code


# antlr4 -Dlanguage=Python3 BL.g4 -o bl -visitor
def main(argv):
    input = FileStream(argv[1])
    lexer = BLLexer(input)
    stream = CommonTokenStream(lexer)
    parser = BLParser(stream)

    with open("out.smt2", "w") as output:
        tree = parser.prog()
        output.write(generate_code(tree))


if __name__ == "__main__":
    main(sys.argv)
