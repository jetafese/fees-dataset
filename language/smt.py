from parser.BLVisitor import BLVisitor
from parser.BLListener import BLListener
from parser.BLParser import BLParser
from antlr4 import *


class DeclarationVisitor(BLVisitor):
    def defaultResult(self) -> set[str]:
        return set()

    def aggregateResult(self, aggregate: set[str], nextResult: set[str]):
        if len(aggregate.intersection(nextResult)) > 0:
            raise ValueError(
                f"repeated definition of variables {aggregate.intersection(nextResult)}"
            )

        return aggregate.union(nextResult)

    def visitAssign(self, ctx: BLParser.AssignContext):
        variable_name = ctx.children[1].symbol.text
        return {variable_name}


class SMTVisitor(BLVisitor):
    def defaultResult(self):
        return ""

    def aggregateResult(self, aggregate: str, nextResult: str):
        if len(aggregate) == 0 or len(nextResult) == 0:
            return aggregate + nextResult
        return aggregate + " " + nextResult

    def visitAssigns(self, ctx: BLParser.AssignsContext) -> str:
        return self.visitChildren(ctx)

    def visitExpr(self, ctx: BLParser.ExprContext):
        if len(ctx.children) == 1:
            return self.visitChildren(ctx)

        # expr -> expr '+' multexpr
        # expr -> expr '-' multexpr

        if ctx.children[1].getText() == "+":
            text = "(+ "
        elif ctx.children[1].getText() == "-":
            text = "(- "
        else:
            assert False

        text += self.visitChildren(ctx)
        text += ")"

        return text

    def visitMultexpr(self, ctx: BLParser.MultexprContext):
        if len(ctx.children) == 1:
            return self.visitChildren(ctx)

        # expr -> expr '*' multexpr
        # expr -> expr '/' multexpr

        if ctx.children[1].getText() == "*":
            text = "(* "
        elif ctx.children[1].getText() == "/":
            text = "(/ "
        else:
            assert False

        text += self.visitChildren(ctx)
        text += ")"

        return text

    def visitUnaryexpr(self, ctx: BLParser.UnaryexprContext):
        if isinstance(ctx.children[0], TerminalNode):
            child_type = ctx.children[0].symbol.type
            # unaryexpr -> NUMBER
            # unaryexpr -> IDENTIFIER
            if child_type == BLParser.NUMBER or child_type == BLParser.IDENTIFIER:
                value: str = ctx.children[0].symbol.text
                return value

            # unaryexpr -> ( expr )
            elif child_type == BLParser.literalNames.index("'('"):
                return self.visitChildren(ctx)
            else:
                assert False

        # unaryexpr -> if
        elif isinstance(ctx.children[0], BLParser.IfContext) or isinstance(
            ctx.children[0], BLParser.AssignContext
        ):
            return self.visitChildren(ctx)

    def visitIf(self, ctx: BLParser.IfContext):
        #  if -> if expr COMP expr then expr else expr;

        text = "(ite ("

        comp: str = ctx.children[2].symbol.text
        text += "=" if comp == "==" else comp
        text += " "
        text += self.visitExpr(ctx.children[1])
        text += " "
        text += self.visitExpr(ctx.children[3])
        text += ") "
        text += self.visitExpr(ctx.children[5])
        text += " "
        text += self.visitExpr(ctx.children[7])

        text += ")"

        return text

    def visitAssign(self, ctx: BLParser.AssignContext):
        variable_name = ctx.children[1].symbol.text
        # text = f"(declare-const {variable_name} Real)\n"
        text = ""
        if not isinstance(ctx.children[-1], TerminalNode):
            text += f"(assert (= {variable_name} "
            text += self.visitExpr(ctx.children[-1])
            text += "))"

        return text


def generate_code(tree: BLParser.ProgContext):
    declaration_visitor = DeclarationVisitor()
    variables = declaration_visitor.visit(tree)

    text = "(set-logic  QF_LRA)\n"

    for variable in variables:
        text += f"(declare-const {variable} Real)\n"

    smt_visitor = SMTVisitor()
    text += smt_visitor.visit(tree)

    return text
