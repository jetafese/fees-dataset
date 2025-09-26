# Generated from Lang.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,60,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,1,4,1,18,8,1,11,1,12,1,19,1,2,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,3,2,30,8,2,1,3,1,3,1,3,3,3,35,8,3,1,4,1,4,1,4,3,4,40,8,4,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,49,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,2,1,0,4,5,1,0,6,7,59,0,14,1,
        0,0,0,2,17,1,0,0,0,4,29,1,0,0,0,6,31,1,0,0,0,8,36,1,0,0,0,10,48,
        1,0,0,0,12,50,1,0,0,0,14,15,3,2,1,0,15,1,1,0,0,0,16,18,3,4,2,0,17,
        16,1,0,0,0,18,19,1,0,0,0,19,17,1,0,0,0,19,20,1,0,0,0,20,3,1,0,0,
        0,21,22,5,1,0,0,22,23,5,14,0,0,23,24,5,2,0,0,24,30,3,6,3,0,25,26,
        5,1,0,0,26,27,5,14,0,0,27,28,5,2,0,0,28,30,5,3,0,0,29,21,1,0,0,0,
        29,25,1,0,0,0,30,5,1,0,0,0,31,34,3,8,4,0,32,33,7,0,0,0,33,35,3,8,
        4,0,34,32,1,0,0,0,34,35,1,0,0,0,35,7,1,0,0,0,36,39,3,10,5,0,37,38,
        7,1,0,0,38,40,3,10,5,0,39,37,1,0,0,0,39,40,1,0,0,0,40,9,1,0,0,0,
        41,49,5,13,0,0,42,49,5,14,0,0,43,44,5,8,0,0,44,45,3,6,3,0,45,46,
        5,9,0,0,46,49,1,0,0,0,47,49,3,12,6,0,48,41,1,0,0,0,48,42,1,0,0,0,
        48,43,1,0,0,0,48,47,1,0,0,0,49,11,1,0,0,0,50,51,5,10,0,0,51,52,3,
        6,3,0,52,53,5,16,0,0,53,54,3,6,3,0,54,55,5,11,0,0,55,56,3,6,3,0,
        56,57,5,12,0,0,57,58,3,6,3,0,58,13,1,0,0,0,5,19,29,34,39,48
    ]

class LangParser ( Parser ):

    grammarFileName = "Lang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'let'", "'='", "'<input>'", "'+'", "'-'", 
                     "'*'", "'/'", "'('", "')'", "'if'", "'then'", "'else'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "IDENTIFIER", "OP", "COMP", 
                      "WHITESPACE" ]

    RULE_prog = 0
    RULE_assigns = 1
    RULE_assign = 2
    RULE_expr = 3
    RULE_multexpr = 4
    RULE_unaryexpr = 5
    RULE_if = 6

    ruleNames =  [ "prog", "assigns", "assign", "expr", "multexpr", "unaryexpr", 
                   "if" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    NUMBER=13
    IDENTIFIER=14
    OP=15
    COMP=16
    WHITESPACE=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assigns(self):
            return self.getTypedRuleContext(LangParser.AssignsContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = LangParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.assigns()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assign(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.AssignContext)
            else:
                return self.getTypedRuleContext(LangParser.AssignContext,i)


        def getRuleIndex(self):
            return LangParser.RULE_assigns

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssigns" ):
                listener.enterAssigns(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssigns" ):
                listener.exitAssigns(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssigns" ):
                return visitor.visitAssigns(self)
            else:
                return visitor.visitChildren(self)




    def assigns(self):

        localctx = LangParser.AssignsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assigns)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 16
                self.assign()
                self.state = 19 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(LangParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(LangParser.ExprContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign" ):
                return visitor.visitAssign(self)
            else:
                return visitor.visitChildren(self)




    def assign(self):

        localctx = LangParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.match(LangParser.T__0)
                self.state = 22
                self.match(LangParser.IDENTIFIER)
                self.state = 23
                self.match(LangParser.T__1)
                self.state = 24
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(LangParser.T__0)
                self.state = 26
                self.match(LangParser.IDENTIFIER)
                self.state = 27
                self.match(LangParser.T__1)
                self.state = 28
                self.match(LangParser.T__2)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.MultexprContext)
            else:
                return self.getTypedRuleContext(LangParser.MultexprContext,i)


        def getRuleIndex(self):
            return LangParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = LangParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.multexpr()
            self.state = 34
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 32
                _la = self._input.LA(1)
                if not(_la==4 or _la==5):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 33
                self.multexpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.UnaryexprContext)
            else:
                return self.getTypedRuleContext(LangParser.UnaryexprContext,i)


        def getRuleIndex(self):
            return LangParser.RULE_multexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultexpr" ):
                listener.enterMultexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultexpr" ):
                listener.exitMultexpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultexpr" ):
                return visitor.visitMultexpr(self)
            else:
                return visitor.visitChildren(self)




    def multexpr(self):

        localctx = LangParser.MultexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_multexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.unaryexpr()
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 37
                _la = self._input.LA(1)
                if not(_la==6 or _la==7):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 38
                self.unaryexpr()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LangParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(LangParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(LangParser.ExprContext,0)


        def if_(self):
            return self.getTypedRuleContext(LangParser.IfContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_unaryexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryexpr" ):
                listener.enterUnaryexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryexpr" ):
                listener.exitUnaryexpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryexpr" ):
                return visitor.visitUnaryexpr(self)
            else:
                return visitor.visitChildren(self)




    def unaryexpr(self):

        localctx = LangParser.UnaryexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_unaryexpr)
        try:
            self.state = 48
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 41
                self.match(LangParser.NUMBER)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 42
                self.match(LangParser.IDENTIFIER)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 43
                self.match(LangParser.T__7)
                self.state = 44
                self.expr()
                self.state = 45
                self.match(LangParser.T__8)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 47
                self.if_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LangParser.ExprContext)
            else:
                return self.getTypedRuleContext(LangParser.ExprContext,i)


        def COMP(self):
            return self.getToken(LangParser.COMP, 0)

        def getRuleIndex(self):
            return LangParser.RULE_if

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf" ):
                listener.enterIf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf" ):
                listener.exitIf(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf" ):
                return visitor.visitIf(self)
            else:
                return visitor.visitChildren(self)




    def if_(self):

        localctx = LangParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(LangParser.T__9)
            self.state = 51
            self.expr()
            self.state = 52
            self.match(LangParser.COMP)
            self.state = 53
            self.expr()
            self.state = 54
            self.match(LangParser.T__10)
            self.state = 55
            self.expr()
            self.state = 56
            self.match(LangParser.T__11)
            self.state = 57
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





