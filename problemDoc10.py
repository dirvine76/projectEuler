def main():
	n = int(input('Enter number\n'))
	primeGenerator(n)


def primeGenerator(n):
	numbers = []
	reader = 0
	
	#Creates number list
	for i in range(n):
		numbers.append(i+1)
	
	#Checks if number has been sieved
	for prime in range(1, n):
		if numbers[prime] == '-':
			continue
			
		x = 1
		reader = numbers[prime] + numbers[prime] * x
		
		while reader <= len(numbers):
			numbers[reader-1] = '-'
			x += 1
			reader = numbers[prime] + numbers[prime] * x
			
	numbers[0] = '-'
	
	primeNumbers = []
	
	for item in numbers:
		if item != '-':
			primeNumbers.append(item)
	sum = 0
	for i in primeNumbers:
		sum += i
	
	print(primeNumbers)
	print('There are %s prime numbers below %s' %(len(primeNumbers),n))
	print(sum)
	return primeNumbers

def primeDetect(n):
	primeNumbers = primeGenerator(n+1)
	if n in primeNumbers:
		print('%s is prime' %(n))
	else:
		print('%s is not prime' %(n))
		
if __name__ == '__main__':
	main()