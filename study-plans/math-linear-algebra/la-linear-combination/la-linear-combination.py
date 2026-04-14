import numpy as np

def linear_combination(vectors, coefficients):
    """
    Returns: float64 array, the weighted sum of vectors.
    """

    vectors = np.array(vectors, dtype=float)
    coefficients = np.array(coefficients, dtype=float)
    result = np.zeros(vectors.shape[1:])

    if vectors.shape[0] != coefficients.shape[0]:
        raise ValueError("The columns should be the same")

    for i in range(len(coefficients)):
        result += (vectors[i] * coefficients[i])

    return result