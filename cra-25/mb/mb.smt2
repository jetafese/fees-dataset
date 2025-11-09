(declare-const Bracket_1 Real)
(declare-const Bracket_2 Real)
(declare-const Bracket_3 Real)
(declare-const FinalTaxes Real)
(declare-const Income Real)

(assert (=> (<= Income 47564.0) (and (= Bracket_1 (* 0.108 Income)) (= Bracket_2 0.0) (= Bracket_3 0.0) (= FinalTaxes (+ Bracket_1 Bracket_2 Bracket_3)))))
(assert (=> (and (> Income 47564.0) (<= Income 101200.0)) (and (= Bracket_1 (* 0.108 47564.0)) (= Bracket_2 (* 0.1275 (- Income 47564.0))) (= Bracket_3 0.0) (= FinalTaxes (+ Bracket_1 Bracket_2 Bracket_3)))))
(assert (=> (> Income 101200.0) (and (= Bracket_1 (* 0.108 47564.0)) (= Bracket_2 (* 0.1275 (- 101200.0 47564.0))) (= Bracket_3 (* 0.174 (- Income 101200.0))) (= FinalTaxes (+ Bracket_1 Bracket_2 Bracket_3)))))
