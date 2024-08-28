(define (abs x)
	(if (< x 0)
		(- 0 x)
		x))

(define (count-up n)
	(define (counter k) 
		(print k)
		(if (< k n)
			(counter (+ k 1))))
	(counter 1))



