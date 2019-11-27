def fibo(n):
	curr = 1
	next = 1
	k = 3
	while k <= n:
		curr, next = next, next + curr
		k = k + 1
	return curr
n = 8
print('The', n, 'th fibonacchi number is:', fibo(n))
