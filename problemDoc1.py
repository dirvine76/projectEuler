reader = 1
k = 1
sum = 0

while reader < 1000:
	if reader % 3 == 0 or reader % 5 == 0:
		sum += reader
	reader += 1
print(sum)