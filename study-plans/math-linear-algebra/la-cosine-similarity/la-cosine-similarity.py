import numpy as np

def cosine_similarity(a, b):
    """
    Returns: float in [-1, 1], cosine similarity between a and b.
    """

    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)

    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        return 0

    similarity = np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

    return similarity
    
    