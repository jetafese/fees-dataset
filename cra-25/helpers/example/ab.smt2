; -----------------------------
; Variable Declarations
; -----------------------------
(declare-const Income Real)
(declare-const FinalTaxes Real)
(declare-const Bracket_1 Real)
(declare-const Bracket_2 Real)
(declare-const Bracket_3 Real)
(declare-const Bracket_4 Real)
(declare-const Bracket_5 Real)
(declare-const Bracket_6 Real)

; -----------------------------
; Alberta Income Tax 2025 Implicative Tree
; -----------------------------
; If-then structure representing the progressive tax calculation

(assert
  (and
    ; Bracket 1: up to $60,000 at 8%
    (=> (<= Income 60000)
        (= FinalTaxes (* 0.08 Income)))

    ; Bracket 2: $60,000 < Income <= $151,234
    (=> (and (> Income 60000) (<= Income 151234))
        (and
          (= Bracket_1 (* 0.08 60000))
          (= Bracket_2 (* 0.10 (- Income 60000)))
          (= FinalTaxes (+ Bracket_1 Bracket_2))
        )
    )

    ; Bracket 3: $151,234 < Income <= $181,481
    (=> (and (> Income 151234) (<= Income 181481))
        (and
          (= Bracket_1 (* 0.08 60000))
          (= Bracket_2 (* 0.10 (- 151234 60000)))
          (= Bracket_3 (* 0.12 (- Income 151234)))
          (= FinalTaxes (+ Bracket_1 Bracket_2 Bracket_3))
        )
    )

    ; Bracket 4: $181,481 < Income <= $241,974
    (=> (and (> Income 181481) (<= Income 241974))
        (and
          (= Bracket_1 (* 0.08 60000))
          (= Bracket_2 (* 0.10 (- 151234 60000)))
          (= Bracket_3 (* 0.12 (- 181481 151234)))
          (= Bracket_4 (* 0.13 (- Income 181481)))
          (= FinalTaxes (+ Bracket_1 Bracket_2 Bracket_3 Bracket_4))
        )
    )

    ; Bracket 5: $241,974 < Income <= $362,961
    (=> (and (> Income 241974) (<= Income 362961))
        (and
          (= Bracket_1 (* 0.08 60000))
          (= Bracket_2 (* 0.10 (- 151234 60000)))
          (= Bracket_3 (* 0.12 (- 181481 151234)))
          (= Bracket_4 (* 0.13 (- 241974 181481)))
          (= Bracket_5 (* 0.14 (- Income 241974)))
          (= FinalTaxes (+ Bracket_1 Bracket_2 Bracket_3 Bracket_4 Bracket_5))
        )
    )

    ; Bracket 6: Income > $362,961
    (=> (> Income 362961)
        (and
          (= Bracket_1 (* 0.08 60000))
          (= Bracket_2 (* 0.10 (- 151234 60000)))
          (= Bracket_3 (* 0.12 (- 181481 151234)))
          (= Bracket_4 (* 0.13 (- 241974 181481)))
          (= Bracket_5 (* 0.14 (- 362961 241974)))
          (= Bracket_6 (* 0.15 (- Income 362961)))
          (= FinalTaxes (+ Bracket_1 Bracket_2 Bracket_3 Bracket_4 Bracket_5 Bracket_6))
        )
    )
  )
)
