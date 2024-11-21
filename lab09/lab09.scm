(define (over-or-under num1 num2) 
(cond 
((< num1 num2) -1)
((= num1 num2) 0)
((> num1 num2) 1)
)
)

(define (make-adder num) 
(lambda(num2) (+ num2 num))
; (define (give_me_one_more num2) (+ num2 num))
; give_me_one_more
)

(define (composed f g) 
(lambda (x) (f (g x)))
)


(define (repeat f n) 
(define (returnme x)
(define (r X N) (if (= N 0) X (r (f X) (- N 1))))
(r x n)
)
returnme
)


(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
(if
(or (> a b) (= a b)) 
(if (= (modulo a b) 0) b (gcd b (modulo a b)))
(gcd b a)
)
)


