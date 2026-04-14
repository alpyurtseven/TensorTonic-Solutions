import numpy as np

def outer_product(u, v):
    """
    Returns: float64 matrix of shape (m, n), the outer product u v^T.
    """
    u = np.array(u, dtype= float)
    v = np.array(v, dtype= float)
    result = np.empty((u.shape[0], v.shape[0]))

    for i in range(u.shape[0]):
        for j in range(v.shape[0]):
            result[i, j] = u[i] * v[j]
    
    return result