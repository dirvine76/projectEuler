numbers = open("numbers.txt", "r")

numList = numbers.readlines()

sum = 0

for num in numList:
	digits = int(num)
	sum += digits
	
stringNum = str(sum)
print(stringNum[0:10])