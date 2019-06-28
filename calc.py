def function(A, B, C):
	print("A = ",A)
	print("B = ",B)
	print("C = ",C)
	A = B
	B = C
	C = C
	print("C = A = ", A)
	return A*B*C*A

value = function(1,2,3) 
print("A*B*C*A=", value)


