import math

def produceTriangleNum(n):
	triangleNum = 0
	for i in range(n):
		triangleNum += i + 1
	return triangleNum

def findDivisors(triangleNum):
	i = 1
	divisors = 0	
	while i <= math.sqrt(triangleNum):
		if (triangleNum % i) == 0:
			divisors += 1
			
			if (triangleNum / i) != i:
				divisors += 1
		i += 1
		
	return divisors
			
n = 0

while True:
	n += 1
	triangleNum = produceTriangleNum(n)
	if findDivisors(triangleNum) > 500:
		print('Number is %d' %(triangleNum))
		break
