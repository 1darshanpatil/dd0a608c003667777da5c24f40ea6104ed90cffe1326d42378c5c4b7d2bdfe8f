from p_of_7 import *

def p_8(n):
    q_8 = q(n, 8)
    s = 0
    for u in range(q_8):
        s += p_7(n - 8 * u - 1)
    return s

if __name__ == "__main__":
    N = int(input("Enter the value of N: "))
    print(p_8(N))