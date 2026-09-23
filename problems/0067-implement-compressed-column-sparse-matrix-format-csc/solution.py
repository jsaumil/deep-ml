import numpy as np
def compressed_col_sparse_matrix(dense_matrix):
	matrix = np.array(dense_matrix)
	vals = []
	row_idx = []
	col_ptr = [0]
	for i in range(matrix.shape[1]):
		col = matrix[:,i]
		for j in range(len(col)):
			if col[j] != 0:
				vals.append(int(col[j]))
				row_idx.append(j)
		col_ptr.append(len(vals))
	
	return vals, row_idx, col_ptr