(define (fact n)
	(if (= n 0)
		1
		(* n (fact (- n 1)))))

(define (fact2 n)
	(define (fact-tail n result)
		(if (<= n 1)
			result
			(fact-tail (- n 1) (* n result))))
	(fact-tail n 1))




