grammar BL;

prog: assigns ;
assigns : (assign)+ ;
assign: 'let' IDENTIFIER '=' expr
        |   'let' IDENTIFIER '=' '<input>'
        ;
expr:   multexpr (('+' | '-') multexpr)? ;
multexpr:   unaryexpr (('*' | '/') unaryexpr)? ;
unaryexpr:  NUMBER
        |   IDENTIFIER
        |   '(' expr ')'
        |   if
        ;

if: 'if' expr COMP expr 'then' expr 'else' expr;

NUMBER: [0-9]+(.[0-9]([0-9])?)? ;
IDENTIFIER: [a-zA-Z][a-zA-Z0-9]* ;
OP: '+'|'-'|'x'|'/' ;
COMP: '>'|'<'|'=='|'<='|'>=' ;
WHITESPACE: [ \t\r\n] -> skip;
