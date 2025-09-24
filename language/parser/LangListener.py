# Generated from Lang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete listener for a parse tree produced by LangParser.
class LangListener(ParseTreeListener):

    # Enter a parse tree produced by LangParser#prog.
    def enterProg(self, ctx:LangParser.ProgContext):
        pass

    # Exit a parse tree produced by LangParser#prog.
    def exitProg(self, ctx:LangParser.ProgContext):
        pass


    # Enter a parse tree produced by LangParser#exprs.
    def enterExprs(self, ctx:LangParser.ExprsContext):
        pass

    # Exit a parse tree produced by LangParser#exprs.
    def exitExprs(self, ctx:LangParser.ExprsContext):
        pass


    # Enter a parse tree produced by LangParser#if.
    def enterIf(self, ctx:LangParser.IfContext):
        pass

    # Exit a parse tree produced by LangParser#if.
    def exitIf(self, ctx:LangParser.IfContext):
        pass


    # Enter a parse tree produced by LangParser#assign.
    def enterAssign(self, ctx:LangParser.AssignContext):
        pass

    # Exit a parse tree produced by LangParser#assign.
    def exitAssign(self, ctx:LangParser.AssignContext):
        pass


    # Enter a parse tree produced by LangParser#expr.
    def enterExpr(self, ctx:LangParser.ExprContext):
        pass

    # Exit a parse tree produced by LangParser#expr.
    def exitExpr(self, ctx:LangParser.ExprContext):
        pass


    # Enter a parse tree produced by LangParser#multexpr.
    def enterMultexpr(self, ctx:LangParser.MultexprContext):
        pass

    # Exit a parse tree produced by LangParser#multexpr.
    def exitMultexpr(self, ctx:LangParser.MultexprContext):
        pass


    # Enter a parse tree produced by LangParser#unaryexpr.
    def enterUnaryexpr(self, ctx:LangParser.UnaryexprContext):
        pass

    # Exit a parse tree produced by LangParser#unaryexpr.
    def exitUnaryexpr(self, ctx:LangParser.UnaryexprContext):
        pass



del LangParser