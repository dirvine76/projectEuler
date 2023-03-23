def findLength(n):
	length = 1
	while n != 1:
		if (n % 2) == 0:
			n = n / 2
			length += 1
		else:
			n = 3 * n + 1
			length += 1
	if n == 1:
		return length
		
maxLength = 0
candidates = []
for i in range(1000000):
	length = findLength(i+1)
	if length > maxLength:
		maxLength = length
		candidates.append(i+1)

print(candidates[-1])