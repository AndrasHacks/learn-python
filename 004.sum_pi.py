def pi_sum(n):
	total, k = 0, 1
	while k <= n:
		total, k = total + 8 / ((4 * k - 3) * (4 * k - 1)), k + 1
	return total
	
print(pi_sum(100000))

# higher order function version
def summation(n, term):
	total, k = 0, 1
	while k <= n:
		total, k = total + term(k), k +1
	return total
	
def pi_sum_term(k):
	return 8 / ((4 * k - 3) * (4 * k - 1))
	
print(summation(1e6, pi_sum_term))
