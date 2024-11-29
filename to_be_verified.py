from math import sin, pi

def q(n, k):
    """
    Safe division function for integer division.
    Returns n // k if k > 0, otherwise returns 0.

    Parameters:
    n (int): Numerator
    k (int): Denominator

    Returns:
    int: Result of n // k or 0 if k is 0.
    """
    return n // k if k > 0 else 0


def p_of_n_k(n, k):
    """
    Recursive function to compute the value of p(n, k) based on the given logic.

    Parameters:
    n (int): Total number
    k (int): Number of partitions

    Returns:
    int: Computed value of p(n, k).
    """
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


if __name__ == "__main__":
    # Main execution block for user input
    try:
        N = int(input("Enter the value of N: "))
        K = int(input("Enter the value of K: "))
        if K > N:
            print("K cannot be greater than N. Please try again.")
        else:
            result = p_of_n_k(N, K)
            print(f"Value of p({N}, {K}): {result}")
    except ValueError:
        print("Invalid input. Please enter integers for N and K.")