import numpy as np
np.random.seed(123)  # Must be FIRST after import

# Verify clean state
rng = np.random.default_rng(123)  # Alternative reproducible generator
data = rng.standard_normal(10)

# OR traditional method (must be first):
data = np.random.randn(10)  # Only works if seed applied immediately after import

print("First 3:", data[:3])
np.savetxt("output_correct.txt", data)
