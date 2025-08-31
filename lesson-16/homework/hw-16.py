# 1. Convert List to 1D Array
# Write a NumPy program to convert a list of numeric values into a one-dimensional NumPy array.
# Expected Output:
# Original List: [12.23, 13.32, 100, 36.32] One-dimensional NumPy array: [ 12.23 13.32 100. 36.32]

import numpy as np

list1 = [12.23,13.23,100,36.32]

arr = np.array(list1)
print(arr)

# 2. Create 3x3 Matrix (2?10)
# Write a NumPy program to create a 3x3 matrix with values ranging from 2 to 10.
# Expected Output:
# [[ 2 3 4] [ 5 6 7] [ 8 9 10]]

import numpy as np

arr1 = np.array([[2,3,4],[5,6,7],[8,9,10]])
print(arr1)

# 3. Null Vector (10) & Update Sixth Value
# Write a NumPy program to create a null vector of size 10 and update the sixth value to 11.
# [ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# Update sixth value to 11 [ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

import numpy as np
zr = np.zeros(10)
zr[6] = 11
print(zr)

# 4. Array from 12 to 38
# Write a NumPy program to create an array with values ranging from 12 to 38.
# Expected Output:
# [12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37]

import numpy as np

rn = np.arange(12,38)
print(rn)

# 5. Convert Array to Float Type
# Write a NumPy program to convert an array to a floating type.
# Sample output:
# Original array [1, 2, 3, 4]

import numpy as np

arr2 = np.array([1,2,3,4])

float_arr2 = np.float64(arr2)
print(float_arr2)
print(float_arr2.dtype)

# 6. Celsius to Fahrenheit Conversion
# Write a NumPy program to convert Centigrade degrees into Fahrenheit degrees. Centigrade values are stored in a NumPy array.
# Sample Array [0, 12, 45.21, 34, 99.91] [-17.78, -11.11, 7.34, 1.11, 37.73, 0. ]
# Expected Output:
# Values in Fahrenheit degrees: [ 0. 12. 45.21 34. 99.91 32. ]
# Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]
# Values in Centigrade degrees: [-17.78 -11.11 7.34 1.11 37.73 0. ]
# Values in Fahrenheit degrees: [-0. 12. 45.21 34. 99.91 32. ]

import numpy as np

cl1 = np.array([0, 12, 45.21, 34, 99.91])
cl2 = np.array([-17.78, -11.11, 7.34, 1.11, 37.73, 0. ])
# F = (C × 9/5) + 32
fh1 = (cl1 * 9/5) + 32
fh2 = (cl2 * 9/5) + 32
print(fh1)
print(fh2)

# 7. Append Values to Array (Do self-tudy)
# Write a NumPy program to append values to the end of an array.
# Expected Output:
# Original array: [10, 20, 30]
# After append values to the end of the array: [10 20 30 40 50 60 70 80 90]

import numpy as np

org_arr = np.array([10, 20, 30])
in_arr = np.append(org_arr,[40,50,60,70,80,90])
print(org_arr)
print(in_arr)

# 8. Array Statistical Functions (Do self-tudy)
# Create a random NumPy array of 10 elements and calculate the mean, median, and standard deviation of the array.

import numpy as np

rnd = np.random.randint(1,100, size=10)
print(f'Numbers: {rnd}')
mn = np.mean(rnd)
md = np.median(rnd)
std = np.std(rnd)
print(f'Mean: {mn}')
print(f'Median: {md}')
print(f'Standard Deviation: {std}')

# 9 Find min and max
# Create a 10x10 array with random values and find the minimum and maximum values.

import numpy as np

arr = np.random.randint(1,100,size=(10,10))
print(arr)
print(arr.max())
print(arr.min())

# 10. Create a 3x3x3 array with random values.
import numpy as np

arr1 = np.random.randint(1,100, size=(3,3,3))

print(arr1)
