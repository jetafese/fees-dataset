(set-logic  QF_LIRA)
(declare-const weight Real)
(declare-const fee Real)
(declare-const MAX Real)

(assert (= fee
    (ite
        (<= weight 1)
        4.47
        (ite
            (<= weight 2)
            5.22
            (ite
                (<= weight 3)
                5.97
                (ite
                    (<= weight 4)
                    6.72
                    (ite
                        (<= weight 5)
                        7.47
                        MAX
                    )
                )
            )
        )
    )
    )
)
(assert (<= weight 5))