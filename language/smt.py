from dataclasses import dataclass

from bl.BLVisitor import BLVisitor
from bl.BLParser import BLParser
from antlr4 import *


@dataclass
class SMTConfig:
    use_functions: bool = False


@dataclass
class Symbol:
    name: str

    # assume all function args + return types are real numbers
    # non-functions have arity 0
    params: set[str]

    def __hash__(self):
        return hash(self.name)


class UseVisitor(BLVisitor):
    """Visitor for finding sets of variables used in an expression"""

    def defaultResult(self) -> set[str]:
        return set()

    def aggregateResult(self, aggregate: set[str], nextResult: set[str]):
        return aggregate.union(nextResult)

    def visitUnaryexpr(self, ctx: BLParser.UnaryexprContext):
        if isinstance(ctx.children[0], TerminalNode):
            child_type = ctx.children[0].symbol.type
            # unaryexpr -> NUMBER
            # unaryexpr -> IDENTIFIER
            if child_type == BLParser.IDENTIFIER:
                value: str = ctx.children[0].symbol.text
                return {value}

        return self.visitChildren(ctx)


class DeclarationVisitor(BLVisitor):
    def defaultResult(self) -> set[Symbol]:
        return set()

    def aggregateResult(self, aggregate: set[Symbol], nextResult: set[Symbol]):
        if len(aggregate.intersection(nextResult)) > 0:
            raise ValueError(
                f"repeated definition of variables {aggregate.intersection(nextResult)}"
            )

        return aggregate.union(nextResult)

    def visitAssign(self, ctx: BLParser.AssignContext):
        variable_name = ctx.children[1].symbol.text
        args = UseVisitor().visitExpr(ctx.children[-1])

        return {Symbol(variable_name, args)}


class SMTVisitor(BLVisitor):
    def __init__(self, symbols: set[Symbol], config: SMTConfig):
        self._symbols = {symbol.name: symbol for symbol in symbols}
        self._config = config

    def defaultResult(self):
        return ""

    def aggregateResult(self, aggregate: str, nextResult: str):
        if len(aggregate) == 0 or len(nextResult) == 0 or aggregate[-1] == "\n":
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
        if self._config.use_functions:
            return self.visitAssign_functions(ctx)
        else:
            return self.visitAssign_no_functions(ctx)

    def visitAssign_no_functions(self, ctx: BLParser.AssignContext):
        variable_name = ctx.children[1].symbol.text
        # if last child is terminal, we are declaring an input variable
        # declaration codegen is handled by the DeclarationVisitor, so we don't
        # need to add anything

        if isinstance(ctx.children[-1], TerminalNode):
            return ""

        text = f"(assert (= {variable_name} "
        text += self.visitExpr(ctx.children[-1])
        text += "))"

        return text

    def visitAssign_functions(self, ctx: BLParser.AssignContext):
        variable_name = ctx.children[1].symbol.text
        if isinstance(ctx.children[-1], TerminalNode):
            return ""

        param_string = " ".join(
            f"({param} Real)" for param in self._symbols[variable_name].params
        )

        application_string = (
            f"{variable_name} {' '.join(list(self._symbols[variable_name].params))}"
        )

        """
        (assert (forall ((max Real) (weight Real)) (= (fee_bl max weight) (
            ite (<= weight 1) 4.47 (ite (<= weight 2) 5.22 (ite (<= weight 3) 5.97 (ite (<= weight 4) 6.72 (ite (<= weight 5) 7.47 max))))
        ))))
        """

        expr_string = self.visitExpr(ctx.children[-1])

        return f"(assert (forall ({param_string}) (= ({application_string}) {expr_string})))"


class SMTCompiler:
    def __init__(self, config: SMTConfig | None = None):
        self._config = config or SMTConfig()

    def generate_code(self, tree: BLParser.ProgContext):
        declaration_visitor = DeclarationVisitor()
        symbols: set[Symbol] = declaration_visitor.visit(tree)

        # text = "(set-logic  QF_LRA)\n"
        text = ""

        for symbol in symbols:
            if not self._config.use_functions:
                text += f"(declare-const {symbol.name} Real)\n"
            elif (
                self._config.use_functions and len(symbol.params) > 0
            ):  # self._config.use_functions and len(symbol.params) > 0
                text += f"(declare-fun {symbol.name} ({' '.join(['Real'] * len(symbol.params))}) Real)\n"

        smt_visitor = SMTVisitor(symbols, self._config)
        text += smt_visitor.visit(tree)

        return text
