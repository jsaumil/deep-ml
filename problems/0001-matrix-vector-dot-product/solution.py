def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	output = [0]*len(a)
	if len(a[0]) != len(b):
		return -1
	for i in range(len(a)):
		row = a[i]
		for j in range(len(b)):
			output[i] = output[i] + b[j]*row[j]
	return output 