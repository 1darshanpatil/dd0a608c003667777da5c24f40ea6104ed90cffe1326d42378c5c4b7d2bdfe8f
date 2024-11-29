import numpy as np
import sys

# Parse command-line arguments
if len(sys.argv) != 3:
    print("Usage: python script_name.py <N> <K>")
    sys.exit(1)

# Convert arguments to integers
N = int(sys.argv[1])
K = int(sys.argv[2]) 

# Initialize the 2D NumPy array
p = np.zeros((N + 1, N + 1), dtype=int)

# Set base cases
for i in range(N + 1):
    p[i, 1] = 1
    p[i, i] = 1

# Compute the values using the recurrence relation
for n in range(2, N + 1):
    for k in range(2, n + 1):
        p[n, k] = p[n - 1, k - 1] + p[n - k, k]

# Compute the sum of p[N][0] to p[N][N]
sum_of_row_N = np.sum(p[N, :])  # Sums over all columns of row N

# Output the results
print(f"Sum of all sub-arrays for row {N}: {sum_of_row_N}")
print(f"Value of p[{N}][{K}]: {p[N][K]}")