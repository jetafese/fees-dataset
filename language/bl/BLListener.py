# Generated from BL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BLParser import BLParser
else:
    from BLParser import BLParser

# This class defines a complete listener for a parse tree produced by BLParser.
class BLListener(ParseTreeListener):

    # Enter a parse tree produced by BLParser#prog.
    def enterProg(self, ctx:BLParser.ProgContext):
        pass

    # Exit a parse tree produced by BLParser#prog.
    def exitProg(self, ctx:BLParser.ProgContext):
        pass


    # Enter a parse tree produced by BLParser#assigns.
    def enterAssigns(self, ctx:BLParser.AssignsContext):
        pass

    # Exit a parse tree produced by BLParser#assigns.
    def exitAssigns(self, ctx:BLParser.AssignsContext):
        pass


    # Enter a parse tree produced by BLParser#assign.
    def enterAssign(self, ctx:BLParser.AssignContext):
        pass

    # Exit a parse tree produced by BLParser#assign.
    def exitAssign(self, ctx:BLParser.AssignContext):
        pass


    # Enter a parse tree produced by BLParser#expr.
    def enterExpr(self, ctx:BLParser.ExprContext):
        pass

    # Exit a parse tree produced by BLParser#expr.
    def exitExpr(self, ctx:BLParser.ExprContext):
        pass


    # Enter a parse tree produced by BLParser#multexpr.
    def enterMultexpr(self, ctx:BLParser.MultexprContext):
        pass

    # Exit a parse tree produced by BLParser#multexpr.
    def exitMultexpr(self, ctx:BLParser.MultexprContext):
        pass


    # Enter a parse tree produced by BLParser#unaryexpr.
    def enterUnaryexpr(self, ctx:BLParser.UnaryexprContext):
        pass

    # Exit a parse tree produced by BLParser#unaryexpr.
    def exitUnaryexpr(self, ctx:BLParser.UnaryexprContext):
        pass


    # Enter a parse tree produced by BLParser#if.
    def enterIf(self, ctx:BLParser.IfContext):
        pass

    # Exit a parse tree produced by BLParser#if.
    def exitIf(self, ctx:BLParser.IfContext):
        pass



del BLParser