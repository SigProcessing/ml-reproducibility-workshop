import numpy as np
import matplotlib.pyplot as plt

# Generate random data
tmp1 = np.random.rand(10)
tmp2 = np.random.rand(10)

# Compute element-wise sum
res1 = []
for i in range(len(tmp1)):
    res1.append(tmp1[i] + tmp2[i])

# Compute element-wise product
res2 = []
for i in range(len(tmp1)):
    res2.append(tmp1[i] * tmp2[i])

# Compute element-wise mean
res3 = []
for i in range(len(tmp1)):
    res3.append((tmp1[i] + tmp2[i]) / 2)

# Plot results
plt.figure()
plt.plot(res1, label="Sum")
plt.plot(res2, label="Product")
plt.plot(res3, label="Mean")
plt.legend()
plt.show()

# Save figure
plt.savefig("plot.png")