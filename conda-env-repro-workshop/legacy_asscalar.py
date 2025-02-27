import numpy as np

# Create a sample array
arr = np.array([1, 2, 3])

# Use the deprecated numpy.asscalar function
scalar = np.asscalar(arr[0])
print("Scalar value:", scalar)