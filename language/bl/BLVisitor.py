# Generated from BL.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .BLParser import BLParser
else:
    from BLParser import BLParser

# This class defines a complete generic visitor for a parse tree produced by BLParser.

class BLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BLParser#prog.
    def visitProg(self, ctx:BLParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BLParser#assigns.
    def visitAssigns(self, ctx:BLParser.AssignsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BLParser#assign.
    def visitAssign(self, ctx:BLParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BLParser#expr.
    def visitExpr(self, ctx:BLParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BLParser#multexpr.
    def visitMultexpr(self, ctx:BLParser.MultexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BLParser#unaryexpr.
    def visitUnaryexpr(self, ctx:BLParser.UnaryexprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BLParser#if.
    def visitIf(self, ctx:BLParser.IfContext):
        return self.visitChildren(ctx)



del BLParser