(set-logic QF_LIRA)

(declare-fun fee_nl (Real Real) Real)
(assert (forall ((weight Real) (max Real)) 
( = (fee_nl weight max)
(ite (<= weight 1)
      4.47
      (ite (and (> weight 1) (<= weight 2))
          5.22
          (ite (and (> weight 2) (<= weight 3))
              5.97
              (ite (and (> weight 3) (<= weight 4))
                  6.72
                  (ite (and (> weight 4) (<= weight 5))
                      7.47
                      max)))))
)
))
