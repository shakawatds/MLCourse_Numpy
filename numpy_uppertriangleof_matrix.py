# -*- coding: utf-8 -*-
"""Numpy_UpperTriangleOf Matrix.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dCDoIG6qqNoznXhdR0Zbx_FgnWvb0zOP
"""

# Example 20: NumPy - Extracting Upper Triangle of a Matrix
import numpy as np

# Creating a square matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Extracting the upper triangle (above the main diagonal)
upper_triangle = np.triu(matrix)

print('Upper Triangle of the Matrix:\n', upper_triangle)

