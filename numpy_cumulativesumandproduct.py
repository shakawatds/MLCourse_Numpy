# -*- coding: utf-8 -*-
"""Numpy_CumulativeSumAndProduct.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1B7GSmXVdxZPLqC3euFFUpbXAIAFrZHRk
"""

# Example 20: NumPy - Cumulative Sum and Product
import numpy as np

# Creating an array
array = np.array([1, 2, 3, 4])

# Calculating cumulative sum and product
cumulative_sum = np.cumsum(array)
cumulative_product = np.cumprod(array)

print('Cumulative Sum:', cumulative_sum)
print('Cumulative Product:', cumulative_product)