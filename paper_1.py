from math import floor
import numpy as np
import random
from tabulate import tabulate

# Define the division logic
q = lambda n, k: n // k

# Recursive function to compute p_k(n)
def compute_p_k(n, k):
    if k == 3:
        # Base case for p_3(n)
        q_3 = q(n, 3)
        s = 0
        for i in range(1, q_3 + 1):
            s += q(n - i, 2) - (i - 1)
        return s
    else:
        # Recursive computation for p_k(n)
        q_k = q(n, k)
        s = 0
        for u in range(q_k):
            s += compute_p_k(n - k * u - 1, k - 1)
        return s

# Function to compute the number of partitions into exactly k parts
# Euler's Identity of Partition of Integers
def partitions_into_k_parts(n, k):
    dp = [[0] * (k + 1) for _ in range(n + 1)]
    dp[0][0] = 1  # Base case: 0 can be partitioned into 0 parts in 1 way

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            if i >= j:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - j][j]
            else:
                dp[i][j] = 0
    return dp[n][k]

# Test function to compare compute_p_k with partitions_into_k_parts
def test_compute_p_k():
    MAX_N = 100  # Reduce for quicker testing (adjustable)
    num_tests = 750  # Number of test cases
    random_values = []
    mismatches = []

    for _ in range(num_tests):
        n = random.randint(3, MAX_N)  # Random n between 3 and MAX_N
        k = random.randint(3, n)  # Random k between 3 and n
        
        # Compute using both methods
        result_p_k = compute_p_k(n, k)
        result_partition = partitions_into_k_parts(n, k)
        
        # Append to results
        random_values.append([n, k, result_p_k, result_partition])
        
        # Check for mismatches
        if result_p_k != result_partition:
            mismatches.append((n, k, result_p_k, result_partition))
    
    # Convert results to numpy array
    data = np.array(random_values, dtype=object)
    
    # Display results in a table
    headers = ["n", "k", "compute_p_k", "partitions_into_k_parts"]
    print(tabulate(data, headers=headers, tablefmt="grid"))

    # Print mismatches
    if mismatches:
        print("\nMismatches Found:")
        print(tabulate(mismatches, headers=headers, tablefmt="grid"))
    else:
        print("\nAll results match!")

if __name__ == "__main__":
    test_compute_p_k()