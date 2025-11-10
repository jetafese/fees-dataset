<role>
You are a tax expert who writes tax programs using BL
</role>

<instructions>
1. Write a program to compute how much taxes are due in the output variable
(fee_bl) using the Business Language BL. The Antlr grammar for BL is provided
below:
<grammar>
prog: assigns ;
assigns : (assign)+ ;
assign: 'let' IDENTIFIER '=' expr | 'let' IDENTIFIER '=' '<input>' ;
expr: multexpr (('+' | '-') multexpr)? ;
multexpr: unaryexpr (('*' | '/') unaryexpr)? ;
unaryexpr: NUMBER | IDENTIFIER | '(' expr ')' | if ;
if: 'if' expr COMP expr 'then' expr 'else' expr;
NUMBER: [0-9]+(.[0-9]([0-9])?)? ;
IDENTIFIER: [a-zA-Z][a-zA-Z0-9]* ;
OP: '+'|'-'|'x'|'/' ;
COMP: '>'|'<'|'=='|'<='|'>=' ;
WHITESPACE: [ \t\r\n] -> skip;
</grammar>
</instructions>

<example>
<input>
<description>
Tax rate,Taxable income threshold
2.00%, on the portion of taxable income that is $1000 or less, plus
4.00%, on the portion of taxable income over $1000 up to $6000 plus
5.00%, on the portion of taxable income over $6000
</description>
</input>

<output>
<program>
let income = <input>
let sin = <input>

let p2 = 0.02 * (if income > 1000 then 1000 else income)
let p4 = if income > 1000 then 0.04 * ((if income > 6000 then 6000 else income) - 1000) else 0
let p5 = if income > 6000 then 0.05 * (income - 6000) else 0

let fee_bl = p2 + p4 + p5
</program>
</output>

<note>
Input variables: income (taxable income)
Tax brackets: Progressive tax calculation across 5 income brackets
Final output: Stored in the fee_bl
</note>
</example>


Now you generate the output for the following input. Please ensure to also have
<output> tags in your final response.
<input>
<description>
${description}
</description>
</input>
