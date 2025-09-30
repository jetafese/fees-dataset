(set-logic  QF_LIRA)
(declare-const weigh Real)
(declare-const fee_nl Real)

(assert (=> (<= weigh 1) (= fee_nl 4.47)))
(assert (=> (and (<= weigh 2) (> weigh 1)) (= fee_nl 5.22)))
(assert (=> (and (<= weigh 3) (> weigh 2)) (= fee_nl 5.97)))
(assert (=> (and (<= weigh 4) (> weigh 3)) (= fee_nl 6.72)))
(assert (=> (and (<= weigh 5) (> weigh 4)) (= fee_nl 7.47)))
