# -*- coding: utf-8 -*-
"""Numpy_FlatteningMultiDimArray.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B7GSmXVdxZPLqC3euFFUpbXAIAFrZHRk
"""

# Example 26: NumPy - Flattening a Multi-dimensional Array
import numpy as np

# Creating a 2D array
array_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Flattening the array
flattened_array = array_2d.flatten()

print('Flattened Array:', flattened_array)