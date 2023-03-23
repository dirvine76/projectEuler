unitKey = [0,3,3,5,4,4,3,5,5,4,3,6,6, 8, 8, 7, 7, 9, 8, 8]
tenKey = [0, 0, 6, 6, 5, 5, 5, 8, 6, 6]


def splitNum(n):
	sum = 0
	thousands = n // 1000
	hundreds = (n // 100) - (thousands * 10)
	tens = (n // 10) - (hundreds * 10) - (thousands * 100)
	units = 0
	if (n % 100) < 20:
		sum += unitKey[n % 100]
	else:
		units = n % 10
	if hundreds > 0:
		sum += 10
	if thousands > 0:
		sum += 8
	
	sum += thousands * 3 + unitKey[hundreds] + tenKey[tens] + units
	return sum
	
sum = 0
for i in range(1000):
	sum += splitNum(i+1)
	
print(sum)