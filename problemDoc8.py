NUM = int(input())
NUMlist = [int(d) for d in str(NUM)]

maxProduct = 1
print(NUMlist)
for number in range(len(NUMlist)-12):
	currentProduct  = 1
	for element in range(13):
		currentProduct *= NUMlist[number + element]
	if currentProduct > maxProduct:
		maxProduct = currentProduct
print(maxProduct)