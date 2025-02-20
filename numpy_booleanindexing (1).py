# -*- coding: utf-8 -*-
"""Numpy_Booleanindexing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B7GSmXVdxZPLqC3euFFUpbXAIAFrZHRk
"""

# Example 3: NumPy - Boolean Indexing
import numpy as np

# Creating an array
array = np.array([10, 15, 20, 25, 30])

# Boolean indexing
greater_than_20 = array[array > 20]

print('Elements Greater Than 20:', greater_than_20)