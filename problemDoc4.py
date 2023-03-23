import math

def detectPrime(n):
	for i in range(int(math.sqrt(n))):
		if n % (i + 1) == 0 and i + 1 != 1:
			return False
	return True
	
	
def productof3digits(n):
	base = int(n/99)
	for i in range(base):
		if n % (base - i) == 0 and 100 < base - i < 1000 and 100 < n / (base - i) < 1000:
			return True

for i in range(990000):
	num = 990000 - i
	strnum = str(num)
	a = strnum
	b = strnum[::-1]
	if a == b and productof3digits(num) == True:
		print(num)
		break
		
		