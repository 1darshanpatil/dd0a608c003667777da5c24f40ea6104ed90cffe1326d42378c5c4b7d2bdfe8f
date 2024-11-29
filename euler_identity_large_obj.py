import numpy as np

def compute_p(N, K=1):
    # Initialize the 2D NumPy array with dtype=object for arbitrary precision
    p = np.zeros((N + 1, N + 1), dtype=object)

    # Set base cases
    for i in range(N + 1):
        p[i, 1] = 1
        if i > 0:
            p[i, i] = 1

    # Compute the values using the recurrence relation
    for n in range(2, N + 1):
        for k in range(2, n + 1):
            p[n, k] = p[n - 1, k - 1] + p[n - k, k]

    # Compute the sum of p[N][0] to p[N][N]
    sum_of_row_N = sum(p[N, :])  # Sums over all columns of row N

    # Return the results
    return sum_of_row_N, p[N, K]

if __name__ == "__main__":
    # Print instructions for the user
    print("Enter the values of N:")
    print("- For a single value, just enter the integer (e.g., 42)")
    print("- For multiple values, enter them as a comma-separated list (e.g., 42, 53, 13423, 52)")

    # Input from the user for N
    inputs = input("Your input for N: ").strip()

    # Determine if the input is a single number or a list
    if ',' in inputs:
        # Convert input string to a list of integers if comma-separated
        n_values = list(map(int, inputs.split(',')))
    else:
        # Convert single input to a list with one element
        n_values = [int(inputs)]

    # Input from the user for K
    k_input = input("Enter the value of K (or press Enter to default to K=1): ").strip()
    k_value = int(k_input) if k_input else 1  # Default to K=1 if no input is given

    # Compute and display results for each N
    for N in n_values:
        sum_of_row_N, p_n_k = compute_p(N, K=k_value)
        print(f"For N={N} and K={k_value}:")
        print(f"  Sum of all sub-arrays for row {N}: {sum_of_row_N}")
        print(f"  Value of p[{N}][{k_value}]: {p_n_k}")