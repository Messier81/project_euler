'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
'''
import math
def fib():
	limit = 4000000
	phi = (1 + 5 ** 0.5)/2
	'''
	#BRUTE FORCE METHOD
	c = 1
	p = 1
	sum = 0
	while p < 4000000: 
		if p % 2 == 0:
			sum += p

		cp = c + p
		c = p
		p = cp
	print(sum)
	'''

	#MATH APPROACH

	'''
	The number of Fibonacci numbers below x can be found by solving for n in Binet's Fibonacci number formula
	https://en.wikipedia.org/wiki/Jacques_Philippe_Marie_Binet

	This gets more accurate as n gets bigger, our limit is pretty big.

	'''

	num_f = math.floor((math.log(limit * 5 ** 0.5))/math.log(phi) + 0.5)

	'''
	If you look at the Fibonacci sequence, only every third number is even, this is proven easily using number theory.
	So we can reduce the above number by a factorof 3.
	'''
	num_f = num_f / 3

	'''
	Using Binet's Fibonacci number formula (also known by https://en.wikipedia.org/wiki/Abraham_de_Moivre)
	we can get every third Fibonacci numbers upto num_f times and add them up, as an arithmetic sequence.
	'''


	i = 0
	n = 0
	ans = 0
	while i <= num_f:
		n = i
		ans = ans + math.floor(((phi ** (3 * n)) - (((-1 * phi)) ** (-1 * 3 * n))) / (5 ** 0.5))
		i += 1
	print(ans)
	
fib()