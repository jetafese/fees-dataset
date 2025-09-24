grammar Lang;
prog:   exprs ;
exprs:  expr exprs
    |   expr
    ;
if: 'if' expr COMP expr 'then' expr 'else' expr;
assign:     'let' IDENTIFIER '=' expr
        |   'let' IDENTIFIER '=' '<input>'
        ;
expr:    expr '+' multexpr
        |   expr '-' multexpr
        |   multexpr
        ;
multexpr:   multexpr '*' unaryexpr
        |   multexpr '/' unaryexpr
        |   unaryexpr
        ;
unaryexpr:  NUMBER
        |   IDENTIFIER
        |   '(' expr ')'
        |   if
        |   assign
        ;

NUMBER: [0-9]+('.'[0-9][0-9])? ;
IDENTIFIER: [a-zA-Z][a-zA-Z0-9]* ;
OP: '+'|'-'|'x'|'/' ;
COMP: '>'|'<'|'=='|'<='|'>=' ;
WHITESPACE: [ \t\r\n] -> skip;
