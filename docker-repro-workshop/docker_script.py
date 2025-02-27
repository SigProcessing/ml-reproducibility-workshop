import numpy as np
import platform
import sys

print("=======================================")
print("Running inside Docker container")
print(f"Python version: {sys.version}")
print(f"Operating System: {platform.system()} {platform.release()}")
print("=======================================")

# Create a sample array
arr = np.array([1, 2, 3])

# Show NumPy version
print(f"Using NumPy version: {np.__version__}")

# Deprecated function (only works in NumPy 1.15)
scalar = np.asscalar(arr[0])
print("Scalar value:", scalar)