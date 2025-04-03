


NumPy Array Functions
NumPy array functions are the built-in functions provided by NumPy that allow us to create and manipulate arrays, and perform different operations on them.

We will discuss some of the most commonly used NumPy array functions.

Common NumPy Array Functions
There are many NumPy array functions available but here are some of the most commonly used ones.

Array Operations	Functions
Array Creation Functions	np.array(), np.zeros(), np.ones(), np.empty(), etc.
Array Manipulation Functions	np.reshape(), np.transpose(), etc.
Array Mathematical Functions	np.add(), np.subtract(), np.sqrt(), np.power(), etc.
Array Statistical Functions	np.median(), np.mean(), np.std(), and np.var().
Array Input and Output Functions	np.save(), np.load(), np.loadtxt(), etc.


NumPy Array Creation Functions
Array creation functions allow us to create new NumPy arrays. For example,

import numpy as np

# create an array using np.array()
array1 = np.array([1, 3, 5])
print("np.array():\n", array1)

# create an array filled with zeros using np.zeros()
array2 = np.zeros((3, 3))
print("\nnp.zeros():\n", array2)

# create an array filled with ones using np.ones()
array3 = np.ones((2, 4))
print("\nnp.ones():\n", array3)



NumPy Array Mathematical Functions
In NumPy, there are tons of mathematical functions to perform on arrays. For example,

import numpy as np

# create two arrays
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([4, 9, 16, 25, 36])

# add the two arrays element-wise
arr_sum = np.add(array1, array2)

# subtract the array2 from array1 element-wise
arr_diff = np.subtract(array1, array2)

# compute square root of array2 element-wise
arr_sqrt = np.sqrt(array2)


print("\nSum of arrays:\n", arr_sum)
print("\nDifference of arrays:\n", arr_diff)
print("\nSquare root of first array:\n", arr_sqrt)