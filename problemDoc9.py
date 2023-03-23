A = []
B = []
C = []

for i in range(1000):
	A.append(i+1)

for i in range(1000):
	B.append(i+1)
		
for i in range(1000):
	C.append(i+1)
	
Asq = [element ** 2 for element in A]
Bsq = [element ** 2 for element in B]
Csq = [element ** 2 for element in C]

for Asquare in Asq:
	for Bsquare in Bsq:
		if (Asquare + Bsquare) in Csq:
			Csquare = Asquare + Bsquare
			if Asq.index(Asquare) + Bsq.index(Bsquare) + Csq.index(Csquare) + 3 == 1000:
				print((Asq.index(Asquare)+1) * (Bsq.index(Bsquare)+1) * (Csq.index(Csquare)+1))