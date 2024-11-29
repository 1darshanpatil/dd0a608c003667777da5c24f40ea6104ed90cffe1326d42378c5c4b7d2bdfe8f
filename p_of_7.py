from p_of_6 import *

def p_7(n):
    q_7 = q(n, 7)
    s = 0
    for u in range(q_7):
        s += p_6(n - 7 * u - 1)
    return s

if __name__ == "__main__":
    N = int(input("Enter the value of N: "))
    print(p_7(N))