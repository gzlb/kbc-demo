"""
Vectors Module
==============
This module provides functions for vector operations.
"""

import numpy as np

def vector_magnitude(v):
    """
    Calculates the magnitude of vector v.

    Args:
        v (np.ndarray): Input vector.

    Returns:
        float: Magnitude of v.

    Example:
        >>> import numpy as np
        >>> from kbc-demo.vectors import vector_magnitude
        >>> v = np.array([3, 4])
        >>> vector_magnitude(v)
        5.0
    """
    return np.linalg.norm(v)

