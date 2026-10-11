import numpy as np
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    a = np.array(a)
    b = np.array(b)
    _,n = a.shape
    m,_ = b.shape
    if n!=m:
        return -1
    c = a @ b
    return c.tolist()