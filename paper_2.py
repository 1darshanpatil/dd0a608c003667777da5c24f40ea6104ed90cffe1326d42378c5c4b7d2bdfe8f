from math import floor
from functools import lru_cache

class PartitionCalculator:
    def __init__(self):
        # Memoized cache for compute_p_k
        self.cache = {}

    # Division logic
    def q(self, n, k):
        return n // k

    # Compute p_k(n) using memoization
    def compute_p_k(self, n, k):
        # Check for cached result
        if (n, k) in self.cache:
            return self.cache[(n, k)]

        if n < 0:
            return 0  # No partitions possible for negative n
        if k == 3:
            # Base case for p_3(n)
            q_3 = self.q(n, 3)
            s = 0
            for i in range(1, q_3 + 1):
                s += self.q(n - i, 2) - (i - 1)
            self.cache[(n, k)] = s
            return s
        else:
            # Recursive computation for p_k(n)
            q_k = self.q(n, k)
            s = 0
            for u in range(q_k):
                s += self.compute_p_k(n - k * u - 1, k - 1)
            self.cache[(n, k)] = s
            return s

    # Compute the summation of p_3(n) to p_n(n)
    def compute_sum_p_k(self, n):
        total = 0
        for k in range(3, n + 1):
            total += self.compute_p_k(n, k)
        total += self.q(n, 2) + 1  # The partitions into two parts and itself.
        return total


if __name__ == "__main__":
    # Print instructions for the user
    print("Enter the values of N:")
    print("- For a single value, just enter the integer (e.g., 42)")
    print("- For multiple values, enter them as a comma-separated list (e.g., 42, 53, 13423, 52)")

    # Input from the user
    inputs = input("Your input: ").strip()

    # Determine if the input is a single number or a list
    if ',' in inputs:
        # Convert input string to a list of integers if comma-separated
        n_values = list(map(int, inputs.split(',')))
    else:
        # Convert single input to a list with one element
        n_values = [int(inputs)]

    # Create an instance of PartitionCalculator
    calculator = PartitionCalculator()

    # Compute and display the results for each input
    for n in n_values:
        result = calculator.compute_sum_p_k(n)
        print(f"The sum of p_3({n}) to p_{n}({n}) is {result}")