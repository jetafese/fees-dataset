(declare-fun fee_bl (Real Real Real Real Real Real) Real)
(assert (
    forall ((weight Real) (max Real) (weigh Real) (maximus Real) (weights Real) (min Real)) 
    (= (fee_bl weight max weigh maximus weights min) (ite (<= weight 1) 4.47 (ite (<= weight 2) 5.22 (ite (<= weight 3) 5.97 (ite (<= weight 4) 6.72 (ite (<= weight 5) 7.47 max))))))))