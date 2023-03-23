list = [1, 2 ,3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
primes = [2,3,5,7,11,13,17,19]
factors = [1]
def primeFactorise(n):
	if n in primes:
		factors.append(n)
	for prime in primes:
		if n % (prime**4) == 0:
			while factors.count(prime) < 4:
				factors.append(prime)
		elif n % (prime**3) == 0:
			while factors.count(prime) < 3:
				factors.append(prime)
		elif n % (prime**2) == 0:
			while factors.count(prime) < 2:
				factors.append(prime)
		elif n % prime == 0:
			while factors.count(prime) < 1:
				factors.append(prime)
		
	
	
product = 1
for num in list:
	primeFactorise(num)
for factor in factors:
	product *= factor
			
print(factors)
print(product)