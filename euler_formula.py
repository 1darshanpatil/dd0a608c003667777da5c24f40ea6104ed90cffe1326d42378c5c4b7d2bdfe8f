import numpy as np

def compute_euler_identity(N, K):
    """
    Computes the Euler identity and returns the sum of all sub-arrays for row N
    and the specific value at p[N][K].

    Parameters:
    N (int): The row index to compute the sum for.
    K (int): The specific column index in the row to retrieve the value.

    Returns:
    tuple: A tuple containing:
           - sum_of_row_N (int): The sum of all sub-array values for row N.
           - p_N_K (int): The value at p[N][K].
    """
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
    p_N_K = p[N][K]

    return sum_of_row_N, p_N_K