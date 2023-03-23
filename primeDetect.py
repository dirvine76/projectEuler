import primeGeneratorSieve

def gcd(a,b):
	while a!= 0:
		a, b = b%a, a
	return b
	
def isPrime(p, n):
	product = primeGeneratorSieve.primeFactorial(n)
	if gcd(p, product) == None:
		print('%s is prime' %(p))
	else:
		print('%s is not prime' %(p))
	
isPrime(10001237, 10000000)