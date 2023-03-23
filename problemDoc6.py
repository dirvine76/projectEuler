sumofsq = 0
sqofsum = 0


for i in range(100):
	sumofsq += (i+1)**2

for i in range(100):
	sqofsum += (i+1)**3
	
print(sqofsum - sumofsq)