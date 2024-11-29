from math import sin, pi
# Define the division logic safely
def q(n, k):
    return n // k if k > 0 else 0


# Recursive function with proper limits
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

if __name__ == "__main__":
    N = int(input("Enter the value of N: "))
    K = int(input("Enter the value of K: "))
    print(p_of_n_k(N, K))