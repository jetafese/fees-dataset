# Generated from BL.g4 by ANTLR 4.13.2
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
        4,1,17,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,4,1,19,8,1,11,1,12,1,20,1,2,1,2,1,2,1,2,1,2,1,
        2,1,2,1,2,3,2,31,8,2,1,3,1,3,1,3,5,3,36,8,3,10,3,12,3,39,9,3,1,4,
        1,4,1,4,5,4,44,8,4,10,4,12,4,47,9,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,
        3,5,56,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,6,0,0,7,0,2,4,6,
        8,10,12,0,2,1,0,4,5,1,0,6,7,66,0,14,1,0,0,0,2,18,1,0,0,0,4,30,1,
        0,0,0,6,32,1,0,0,0,8,40,1,0,0,0,10,55,1,0,0,0,12,57,1,0,0,0,14,15,
        3,2,1,0,15,16,5,0,0,1,16,1,1,0,0,0,17,19,3,4,2,0,18,17,1,0,0,0,19,
        20,1,0,0,0,20,18,1,0,0,0,20,21,1,0,0,0,21,3,1,0,0,0,22,23,5,1,0,
        0,23,24,5,14,0,0,24,25,5,2,0,0,25,31,3,6,3,0,26,27,5,1,0,0,27,28,
        5,14,0,0,28,29,5,2,0,0,29,31,5,3,0,0,30,22,1,0,0,0,30,26,1,0,0,0,
        31,5,1,0,0,0,32,37,3,8,4,0,33,34,7,0,0,0,34,36,3,8,4,0,35,33,1,0,
        0,0,36,39,1,0,0,0,37,35,1,0,0,0,37,38,1,0,0,0,38,7,1,0,0,0,39,37,
        1,0,0,0,40,45,3,10,5,0,41,42,7,1,0,0,42,44,3,10,5,0,43,41,1,0,0,
        0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,9,1,0,0,0,47,45,1,
        0,0,0,48,56,5,13,0,0,49,56,5,14,0,0,50,51,5,8,0,0,51,52,3,6,3,0,
        52,53,5,9,0,0,53,56,1,0,0,0,54,56,3,12,6,0,55,48,1,0,0,0,55,49,1,
        0,0,0,55,50,1,0,0,0,55,54,1,0,0,0,56,11,1,0,0,0,57,58,5,10,0,0,58,
        59,3,6,3,0,59,60,5,16,0,0,60,61,3,6,3,0,61,62,5,11,0,0,62,63,3,6,
        3,0,63,64,5,12,0,0,64,65,3,6,3,0,65,13,1,0,0,0,5,20,30,37,45,55
    ]

class BLParser ( Parser ):

    grammarFileName = "BL.g4"

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
            return self.getTypedRuleContext(BLParser.AssignsContext,0)


        def EOF(self):
            return self.getToken(BLParser.EOF, 0)

        def getRuleIndex(self):
            return BLParser.RULE_prog

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

        localctx = BLParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.assigns()
            self.state = 15
            self.match(BLParser.EOF)
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
                return self.getTypedRuleContexts(BLParser.AssignContext)
            else:
                return self.getTypedRuleContext(BLParser.AssignContext,i)


        def getRuleIndex(self):
            return BLParser.RULE_assigns

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

        localctx = BLParser.AssignsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assigns)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 17
                self.assign()
                self.state = 20 
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
            return self.getToken(BLParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(BLParser.ExprContext,0)


        def getRuleIndex(self):
            return BLParser.RULE_assign

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

        localctx = BLParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_assign)
        try:
            self.state = 30
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 22
                self.match(BLParser.T__0)
                self.state = 23
                self.match(BLParser.IDENTIFIER)
                self.state = 24
                self.match(BLParser.T__1)
                self.state = 25
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(BLParser.T__0)
                self.state = 27
                self.match(BLParser.IDENTIFIER)
                self.state = 28
                self.match(BLParser.T__1)
                self.state = 29
                self.match(BLParser.T__2)
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
                return self.getTypedRuleContexts(BLParser.MultexprContext)
            else:
                return self.getTypedRuleContext(BLParser.MultexprContext,i)


        def getRuleIndex(self):
            return BLParser.RULE_expr

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

        localctx = BLParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.multexpr()
            self.state = 37
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 33
                    _la = self._input.LA(1)
                    if not(_la==4 or _la==5):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 34
                    self.multexpr() 
                self.state = 39
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

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
                return self.getTypedRuleContexts(BLParser.UnaryexprContext)
            else:
                return self.getTypedRuleContext(BLParser.UnaryexprContext,i)


        def getRuleIndex(self):
            return BLParser.RULE_multexpr

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

        localctx = BLParser.MultexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_multexpr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.unaryexpr()
            self.state = 45
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 41
                    _la = self._input.LA(1)
                    if not(_la==6 or _la==7):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 42
                    self.unaryexpr() 
                self.state = 47
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
            return self.getToken(BLParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(BLParser.IDENTIFIER, 0)

        def expr(self):
            return self.getTypedRuleContext(BLParser.ExprContext,0)


        def if_(self):
            return self.getTypedRuleContext(BLParser.IfContext,0)


        def getRuleIndex(self):
            return BLParser.RULE_unaryexpr

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

        localctx = BLParser.UnaryexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_unaryexpr)
        try:
            self.state = 55
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.match(BLParser.NUMBER)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.match(BLParser.IDENTIFIER)
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.match(BLParser.T__7)
                self.state = 51
                self.expr()
                self.state = 52
                self.match(BLParser.T__8)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 4)
                self.state = 54
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
                return self.getTypedRuleContexts(BLParser.ExprContext)
            else:
                return self.getTypedRuleContext(BLParser.ExprContext,i)


        def COMP(self):
            return self.getToken(BLParser.COMP, 0)

        def getRuleIndex(self):
            return BLParser.RULE_if

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

        localctx = BLParser.IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(BLParser.T__9)
            self.state = 58
            self.expr()
            self.state = 59
            self.match(BLParser.COMP)
            self.state = 60
            self.expr()
            self.state = 61
            self.match(BLParser.T__10)
            self.state = 62
            self.expr()
            self.state = 63
            self.match(BLParser.T__11)
            self.state = 64
            self.expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





