import numpy as np

def euclidean_distance(x, y):
    """
    Returns: float, the Euclidean distance between x and y.
    """
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)

    difference = np.subtract(x, y)
    magnitude = difference.dot(difference)
    distance = np.sqrt(magnitude)
    
    return float(distance)