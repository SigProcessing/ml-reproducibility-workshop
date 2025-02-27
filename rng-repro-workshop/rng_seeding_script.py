import random
import numpy as np
import torch
import tensorflow as tf

# Seeding Python's built-in RNG
random.seed(42)
print("Python random:", random.random())

# Seeding NumPy's legacy RNG (global state)
np.random.seed(42)
print("NumPy (legacy) random:", np.random.rand())

# Seeding NumPy's new Generator API (independent RNG)
rng = np.random.default_rng(42)
print("NumPy (new Generator) random:", rng.random())

# Seeding PyTorch's RNG
torch.manual_seed(42)
print("PyTorch random:", torch.rand(1).item())

# Seeding TensorFlow's RNG
tf.random.set_seed(42)
print("TensorFlow random:", tf.random.uniform((1,)).numpy()[0])