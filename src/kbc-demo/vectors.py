"""
Vectors Module
==============
This module provides functions for vector operations.
"""

import numpy as np

def vector_magnitude(v):
    """
    Calculate the magnitude of vector v.
    
    :param v: Input vector
    :return: Magnitude of v
    """
    return np.linalg.norm(v)
