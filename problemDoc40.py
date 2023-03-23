
integer_list = []
digit_list = []

N = 4000000

for i in range(N):
	integer_list.append(i+1)

for item in integer_list:
	str_num = str(item)
	for i in range(len(str_num)):
		digit_list.append(str_num[i])

for i in range(len(digit_list)):
	digit_list[i] = int(digit_list[i])

product = digit_list[0] * digit_list[9] * digit_list[99] * digit_list[999] * digit_list[9999] * digit_list[99999] * digit_list[999999]
print(product)