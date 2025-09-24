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
        4,1,17,80,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,1,1,1,1,1,1,1,3,1,21,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,
        1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,40,8,3,1,4,1,4,1,4,1,
        4,1,4,1,4,1,4,1,4,1,4,5,4,51,8,4,10,4,12,4,54,9,4,1,5,1,5,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,5,5,65,8,5,10,5,12,5,68,9,5,1,6,1,6,1,6,1,
        6,1,6,1,6,1,6,1,6,3,6,78,8,6,1,6,0,2,8,10,7,0,2,4,6,8,10,12,0,0,
        82,0,14,1,0,0,0,2,20,1,0,0,0,4,22,1,0,0,0,6,39,1,0,0,0,8,41,1,0,
        0,0,10,55,1,0,0,0,12,77,1,0,0,0,14,15,3,2,1,0,15,1,1,0,0,0,16,17,
        3,8,4,0,17,18,3,2,1,0,18,21,1,0,0,0,19,21,3,8,4,0,20,16,1,0,0,0,
        20,19,1,0,0,0,21,3,1,0,0,0,22,23,5,1,0,0,23,24,3,8,4,0,24,25,5,16,
        0,0,25,26,3,8,4,0,26,27,5,2,0,0,27,28,3,8,4,0,28,29,5,3,0,0,29,30,
        3,8,4,0,30,5,1,0,0,0,31,32,5,4,0,0,32,33,5,14,0,0,33,34,5,5,0,0,
        34,40,3,8,4,0,35,36,5,4,0,0,36,37,5,14,0,0,37,38,5,5,0,0,38,40,5,
        6,0,0,39,31,1,0,0,0,39,35,1,0,0,0,40,7,1,0,0,0,41,42,6,4,-1,0,42,
        43,3,10,5,0,43,52,1,0,0,0,44,45,10,3,0,0,45,46,5,7,0,0,46,51,3,10,
        5,0,47,48,10,2,0,0,48,49,5,8,0,0,49,51,3,10,5,0,50,44,1,0,0,0,50,
        47,1,0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,9,1,0,0,
        0,54,52,1,0,0,0,55,56,6,5,-1,0,56,57,3,12,6,0,57,66,1,0,0,0,58,59,
        10,3,0,0,59,60,5,9,0,0,60,65,3,12,6,0,61,62,10,2,0,0,62,63,5,10,
        0,0,63,65,3,12,6,0,64,58,1,0,0,0,64,61,1,0,0,0,65,68,1,0,0,0,66,
        64,1,0,0,0,66,67,1,0,0,0,67,11,1,0,0,0,68,66,1,0,0,0,69,78,5,13,
        0,0,70,78,5,14,0,0,71,72,5,11,0,0,72,73,3,8,4,0,73,74,5,12,0,0,74,
        78,1,0,0,0,75,78,3,4,2,0,76,78,3,6,3,0,77,69,1,0,0,0,77,70,1,0,0,
        0,77,71,1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,0,78,13,1,0,0,0,7,20,39,
        50,52,64,66,77
    ]

class LangParser ( Parser ):

    grammarFileName = "Lang.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'if'", "'then'", "'else'", "'let'", "'='", 
                     "'<input>'", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "IDENTIFIER", "OP", "COMP", 
                      "WHITESPACE" ]

    RULE_prog = 0
    RULE_exprs = 1
    RULE_if = 2
    RULE_assign = 3
    RULE_expr = 4
    RULE_multexpr = 5
    RULE_unaryexpr = 6

    ruleNames =  [ "prog", "exprs", "if", "assign", "expr", "multexpr", 
                   "unaryexpr" ]

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

        def exprs(self):
            return self.getTypedRuleContext(LangParser.ExprsContext,0)


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
            self.exprs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(LangParser.ExprContext,0)


        def exprs(self):
            return self.getTypedRuleContext(LangParser.ExprsContext,0)


        def getRuleIndex(self):
            return LangParser.RULE_exprs

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprs" ):
                listener.enterExprs(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprs" ):
                listener.exitExprs(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprs" ):
                return visitor.visitExprs(self)
            else:
                return visitor.visitChildren(self)




    def exprs(self):

        localctx = LangParser.ExprsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exprs)
        try:
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.expr(0)
                self.state = 17
                self.exprs()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.expr(0)
                pass


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
        self.enterRule(localctx, 4, self.RULE_if)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(LangParser.T__0)
            self.state = 23
            self.expr(0)
            self.state = 24
            self.match(LangParser.COMP)
            self.state = 25
            self.expr(0)
            self.state = 26
            self.match(LangParser.T__1)
            self.state = 27
            self.expr(0)
            self.state = 28
            self.match(LangParser.T__2)
            self.state = 29
            self.expr(0)
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
        self.enterRule(localctx, 6, self.RULE_assign)
        try:
            self.state = 39
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.match(LangParser.T__3)
                self.state = 32
                self.match(LangParser.IDENTIFIER)
                self.state = 33
                self.match(LangParser.T__4)
                self.state = 34
                self.expr(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 35
                self.match(LangParser.T__3)
                self.state = 36
                self.match(LangParser.IDENTIFIER)
                self.state = 37
                self.match(LangParser.T__4)
                self.state = 38
                self.match(LangParser.T__5)
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

        def multexpr(self):
            return self.getTypedRuleContext(LangParser.MultexprContext,0)


        def expr(self):
            return self.getTypedRuleContext(LangParser.ExprContext,0)


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



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LangParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.multexpr(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 50
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = LangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 45
                        self.match(LangParser.T__6)
                        self.state = 46
                        self.multexpr(0)
                        pass

                    elif la_ == 2:
                        localctx = LangParser.ExprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 48
                        self.match(LangParser.T__7)
                        self.state = 49
                        self.multexpr(0)
                        pass

             
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryexpr(self):
            return self.getTypedRuleContext(LangParser.UnaryexprContext,0)


        def multexpr(self):
            return self.getTypedRuleContext(LangParser.MultexprContext,0)


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



    def multexpr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LangParser.MultexprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_multexpr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.unaryexpr()
            self._ctx.stop = self._input.LT(-1)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 64
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = LangParser.MultexprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multexpr)
                        self.state = 58
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 59
                        self.match(LangParser.T__8)
                        self.state = 60
                        self.unaryexpr()
                        pass

                    elif la_ == 2:
                        localctx = LangParser.MultexprContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_multexpr)
                        self.state = 61
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 62
                        self.match(LangParser.T__9)
                        self.state = 63
                        self.unaryexpr()
                        pass

             
                self.state = 68
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
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


        def assign(self):
            return self.getTypedRuleContext(LangParser.AssignContext,0)


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
        self.enterRule(localctx, 12, self.RULE_unaryexpr)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.match(LangParser.NUMBER)
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(LangParser.IDENTIFIER)
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.match(LangParser.T__10)
                self.state = 72
                self.expr(0)
                self.state = 73
                self.match(LangParser.T__11)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.if_()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 5)
                self.state = 76
                self.assign()
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[4] = self.expr_sempred
        self._predicates[5] = self.multexpr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def multexpr_sempred(self, localctx:MultexprContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




