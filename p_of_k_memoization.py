from math import floor
from functools import lru_cache

# Define the division logic
q = lambda n, k: n // k

# Memoized recursive function to compute p_k(n)
@lru_cache(maxsize=None)
def compute_p_k(n, k):
    if n < 0:
        return 0  # No partitions possible for negative n
    if k == 3:
        # Base case for p_3(n)
        q_3 = q(n, 3)
        s = 0
        for i in range(1, q_3 + 1):
            s += q(n - i, 2) - (i - 1)
        return s
    else:
        # Recursive computation for p_k(n) with memoization
        q_k = q(n, k)
        s = 0
        for u in range(q_k):
            s += compute_p_k(n - k * u - 1, k - 1)
        return s

if __name__ == "__main__":
    # Input values
    k = int(input("Enter the value of K: "))
    n = int(input("Enter the value of N: "))

    # Compute and print the result
    result = compute_p_k(n, k)
    print(f"p_{k}({n}) = {result}")