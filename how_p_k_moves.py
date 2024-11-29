import math

def p(n, k, depth=0):
    indent = "  " * depth  # Indentation to show recursion depth
    print(f"{indent}Entering p(n={n}, k={k})")
    
    if k == 0 or n <= 0:
        # Base case: either k is zero or n is non-positive
        print(f"{indent}Base case reached: p(n={n}, k={k}) = 0 (or undefined)")
        return
    
    # Simulate the range for u from 0 to Q_k(n) - sin^2(0.5 * pi * (k - 1))
    # We'll assume Q_k(n) is some function of n and k, e.g., n // k for simplicity.
    # Replace this with actual Q_k(n) if available.
    Q_k_n = n // k
    u_max = Q_k_n - math.sin(math.pi * (k - 1) / 2) ** 2

    u_values = range(int(u_max) + 1)  # Generate u values
    for u in u_values:
        print(f"{indent}  Summing for u={u} in range(0, {int(u_max)})")
        # Recursive call
        p(n - k * u - 1, k - 1, depth + 1)

# Example call
p(10, 5)