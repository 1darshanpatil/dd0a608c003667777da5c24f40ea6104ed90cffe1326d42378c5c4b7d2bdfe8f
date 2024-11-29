import random
from math import sin, pi
from tabulate import tabulate
import numpy as np
q = lambda n, k: n // k if k > 0 else 0

def p_of_n_k(n, k):
    if k == 3:
        q_3 = q(n, 3)
        s = 0
        for j in range(1, q_3 + 1):
            s += q(n - j, 2) - (j - 1)
        return s
    if k == 2:
        return q(n, 2)
    if k == 1:
        return 1
    q_k_of_n = q(n, k)
    delta = int((sin(pi * (k - 1) * 0.5)) ** 2)  # Compute delta
    sm = 0
    for u in range(q_k_of_n - delta + 1):
        sm += p_of_n_k(n - k * u - 1, k - 1)
    return sm

def compute_euler_identity(N, K):
    p = np.zeros((N + 1, N + 1), dtype=int)
    for i in range(N + 1):
        p[i, 1] = 1
        p[i, i] = 1
    for n in range(2, N + 1):
        for k in range(2, n + 1):
            p[n, k] = p[n - 1, k - 1] + p[n - k, k]
    sum_of_row_N = np.sum(p[N, :])  # Sums over all columns of row N
    p_N_K = p[N][K]
    return sum_of_row_N, p_N_K

def generate_random_values(num_tests=100, max_n=100):
    values = []
    for _ in range(num_tests):
        N = random.randint(1, max_n)
        K = random.randint(1, N)
        values.append((N, K))
    return values

def validate(N, K):
    _, euler_value = compute_euler_identity(N, K)
    custom_value = p_of_n_k(N, K)
    return euler_value, custom_value, euler_value == custom_value

if __name__ == "__main__":
    max_n = 100
    num_tests = 501 # To avoid repeatation num_tests <= max_n^2
    test_values = generate_random_values(num_tests, max_n)
    results = []
    print(f"Running {num_tests} validations...")
    for N, K in test_values:
        euler_value, custom_value, is_equal = validate(N, K)
        # Format values to avoid scientific notation
        euler_value_fmt = f"{euler_value:.0f}" if euler_value >= 1e5 else str(euler_value)
        custom_value_fmt = f"{custom_value:.0f}" if custom_value >= 1e5 else str(custom_value)
        results.append([N, K, euler_value_fmt, custom_value_fmt, "Pass" if is_equal else "Fail"])
    # Print results in tabular format
    headers = ["N", "K", "Euler Value", "Custom Value", "Status"]
    print(tabulate(results, headers=headers, tablefmt="grid"))
    all_tests_passed = all(row[4] == "Pass" for row in results)
    if all_tests_passed:
        print("\nAll tests passed! The formula matches Euler's identity.")
    else:
        print("\nSome tests failed. Investigate the discrepancy.")