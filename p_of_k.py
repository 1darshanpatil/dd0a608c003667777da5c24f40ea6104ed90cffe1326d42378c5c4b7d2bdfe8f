from math import floor

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

if __name__ == "__main__":
    # Input values
    print("Please enter the values for n and k, ensuring that k > 2 and k <= n.")
    k = int(input("Enter the value of k: "))
    n = int(input("Enter the value of n: "))
    # Compute and print the result
    result = compute_p_k(n, k)
    print(f"p_{k}({n}) = {result}")