(declare-const Bracket_1 Real)
(declare-const Bracket_2 Real)
(declare-const Bracket_3 Real)
(declare-const FinalTaxes Real)
(declare-const Income Real)

(assert (=> (<= Income 47564.0) (and (= Bracket_1 (* Income 0.108)) (= Bracket_2 0.0) (= Bracket_3 0.0) (= FinalTaxes (+ Bracket_1 Bracket_2 Bracket_3)))))
(assert (=> (and (> Income 47564.0) (<= Income 101200.0)) (and (= Bracket_1 (* 47564.0 0.108)) (= Bracket_2 (* (- Income 47564.0) 0.1275)) (= Bracket_3 0.0) (= FinalTaxes (+ Bracket_1 Bracket_2 Bracket_3)))))
(assert (=> (> Income 101200.0) (and (= Bracket_1 (* 47564.0 0.108)) (= Bracket_2 (* (- 101200.0 47564.0) 0.1275)) (= Bracket_3 (* (- Income 101200.0) 0.174)) (= FinalTaxes (+ Bracket_1 Bracket_2 Bracket_3)))))
