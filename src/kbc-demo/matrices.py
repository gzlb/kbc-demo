"""
Matrices Module
===============
This module provides functions for matrix operations.
"""

import numpy as np

def matrix_addition(A, B):
    """
    Adds two matrices A and B.

    Args:
        A (np.ndarray): First matrix.
        B (np.ndarray): Second matrix.

    Returns:
        np.ndarray: Matrix sum of A and B.

    Example:
        >>> import numpy as np
        >>> from kbc-demo.matrices import matrix_addition
        >>> A = np.array([[1, 2], [3, 4]])
        >>> B = np.array([[5, 6], [7, 8]])
        >>> matrix_addition(A, B)
        array([[ 6,  8],
               [10, 12]])
    """
    return np.add(A, B)

