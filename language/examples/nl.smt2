(set-logic  QF_LIRA)
(declare-const weight Real)
(declare-const fee Real)

(assert (=> (<= weight 1) (= fee 4.47)))
(assert (=> (and (<= weight 2) (> weight 1)) (= fee 5.22)))
(assert (=> (and (<= weight 3) (> weight 2)) (= fee 5.97)))
(assert (=> (and (<= weight 4) (> weight 3)) (= fee 6.72)))
(assert (=> (and (<= weight 5) (> weight 4)) (= fee 7.47)))
