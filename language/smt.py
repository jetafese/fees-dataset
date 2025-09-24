from parser.LangVisitor import LangVisitor
from parser.LangListener import LangListener
from parser.LangParser import LangParser
from antlr4 import *


class DeclarationVisitor(LangVisitor):
    def defaultResult(self) -> set[str]:
        return set()

    def aggregateResult(self, aggregate: set[str], nextResult: set[str]):
        if len(aggregate.intersection(nextResult)) > 0:
            raise ValueError(
                f"repeated definition of variables {aggregate.intersection(nextResult)}"
            )

        return aggregate.union(nextResult)

    def visitAssign(self, ctx: LangParser.AssignContext):
        variable_name = ctx.children[1].symbol.text
        return {variable_name}

    def visitIf(self, ctx: LangParser.IfContext):
        # assert no variables in the condition
        if (
            len(self.visitExpr(ctx.children[1])) != 0
            or len(self.visitExpr(ctx.children[3])) != 0
        ):
            raise ValueError("cannot declare variables in condition")

        return self.visitExpr(ctx.children[5]).union(self.visitExpr(ctx.children[7]))


class SMTVisitor(LangVisitor):
    def defaultResult(self):
        return ""

    def aggregateResult(self, aggregate: str, nextResult: str):
        if len(aggregate) == 0 or len(nextResult) == 0:
            return aggregate + nextResult
        return aggregate + " " + nextResult

    def visitExprs(self, ctx: LangParser.ExprsContext) -> str:
        return self.visitChildren(ctx)

    def visitExpr(self, ctx: LangParser.ExprContext):
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

    def visitMultexpr(self, ctx: LangParser.MultexprContext):
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

    def visitUnaryexpr(self, ctx: LangParser.UnaryexprContext):
        if isinstance(ctx.children[0], TerminalNode):
            child_type = ctx.children[0].symbol.type
            # unaryexpr -> NUMBER
            # unaryexpr -> IDENTIFIER
            if child_type == LangParser.NUMBER or child_type == LangParser.IDENTIFIER:
                value: str = ctx.children[0].symbol.text
                return value

            # unaryexpr -> ( expr )
            elif child_type == LangParser.literalNames.index("'('"):
                return self.visitChildren(ctx)
            else:
                assert False

        # unaryexpr -> if
        elif isinstance(ctx.children[0], LangParser.IfContext) or isinstance(
            ctx.children[0], LangParser.AssignContext
        ):
            return self.visitChildren(ctx)

    def visitIf(self, ctx: LangParser.IfContext):
        #  if -> if expr COMP expr then expr else expr;

        text = "(ite ("

        comp: str = ctx.children[2].symbol.text
        text += comp
        text += " "
        text += self.visitExpr(ctx.children[1])
        text += " "
        text += self.visitExpr(ctx.children[3])
        text += ") "
        text += self.visitExprs(ctx.children[5])
        text += " "
        text += self.visitExprs(ctx.children[7])

        text += ")"

        return text

    def visitAssign(self, ctx: LangParser.AssignContext):
        variable_name = ctx.children[1].symbol.text
        # text = f"(declare-const {variable_name} Real)\n"
        text = ""
        if not isinstance(ctx.children[-1], TerminalNode):
            text += f"(assert (= {variable_name} "
            text += self.visitExpr(ctx.children[-1])
            text += "))"

        return text


def generate_code(tree: LangParser.ProgContext):
    declaration_visitor = DeclarationVisitor()
    variables = declaration_visitor.visit(tree)

    text = ""

    for variable in variables:
        text += f"(declare-const {variable} Real)\n"

    smt_visitor = SMTVisitor()
    text += smt_visitor.visit(tree)

    return text
