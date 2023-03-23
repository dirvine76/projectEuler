num = 2 ** 1000

stringNum = str(num)
stringList = []
for i in stringNum:
	stringList.append(i)

print(stringList)
sum = 0

for num in stringList:
	number = int(num)
	sum += number
	
print(sum)