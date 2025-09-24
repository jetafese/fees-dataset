import sys

from antlr4 import *
from parser.LangLexer import LangLexer
from parser.LangParser import LangParser
from smt import SMTVisitor


def main(argv):
    input = FileStream(argv[1])
    lexer = LangLexer(input)
    stream = CommonTokenStream(lexer)
    parser = LangParser(stream)

    with open("out.prog", "w") as output:
        tree = parser.prog()
        visitor = SMTVisitor()
        output.write(visitor.visit(tree))
        pass


if __name__ == "__main__":
    main(sys.argv)
