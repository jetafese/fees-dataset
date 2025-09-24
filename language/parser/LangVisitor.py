# Generated from Lang.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LangParser import LangParser
else:
    from LangParser import LangParser

# This class defines a complete generic visitor for a parse tree produced by LangParser.

class LangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LangParser#prog.
    def visitProg(self, ctx:LangParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#exprs.
    def visitExprs(self, ctx:LangParser.ExprsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#if.
    def visitIf(self, ctx:LangParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#assign.
    def visitAssign(self, ctx:LangParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#expr.
    def visitExpr(self, ctx:LangParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#multexpr.
    def visitMultexpr(self, ctx:LangParser.MultexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LangParser#unaryexpr.
    def visitUnaryexpr(self, ctx:LangParser.UnaryexprContext):
        return self.visitChildren(ctx)



del LangParser