import math

def detectPrime(n):
	for i in range(int(math.sqrt(n))):
		if n % (i + 1) == 0 and i + 1 != 1:
			return False
	return True
	
def breakdownNum(num):
	base = int(math.sqrt(num))
	for i in range(base):
		if num % (base - i) == 0 and detectPrime(base - i) == True:
			return base - i
			
print(breakdownNum(600851475143))