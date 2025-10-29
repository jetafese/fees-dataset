## Target

This folder introduces the notion of private variables via an example. As we develop the framework for comparing consistency of business logic to code, these `edge` cases that implement temporary/bespoke properties need to be handled.

The reason why this is important is that the business wants to ensure the integrity of their framework, modulo, discounts/promotions.

## Framework

The classic equivalence problem is: given f1(a, b), f2(c, d), prove that f1 and f2 are have the same output for all inputs where we assume that a == c and b == d

A modification of this problem is: given f1(a, b), f2(c, d), prove that f1 and f2 are have the same output for all inputs where only a == c; Admittedly this is a harder problem because you need to find the cases where b == d so that your equivalence holds

This is an opportunity to reframe the problem so that we can find all possible assumptions/cases that need to hold in order for the equivalent to hold. For example, in this folder, we want to establish that in every case where the special restriction is not triggered, the two functions for the tax code are equivalent.

In other words, the queries:
1. f1(a, b) = f2(c, d) is valid, if an only if, Not(special)
2. special => f1(a, b) = f2(c, d) is never the case