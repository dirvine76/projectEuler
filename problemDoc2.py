term = 2
fibs = [1,2]
while fibs[term-1] <= 4000000:
	fibs.append(fibs[term - 1] + fibs[term -2])
	term += 1


sum = 0
k = 0
reader = 3*k + 1
while reader < len(fibs):
	sum += fibs[reader]
	k += 1
	reader = 3*k + 1
print(sum)