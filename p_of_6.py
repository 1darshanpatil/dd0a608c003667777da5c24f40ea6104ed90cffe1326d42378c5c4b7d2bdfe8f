from p_of_5 import *

def p_6(n):
	q_6 = q(n, 6)
	s = 0
	for u in range(q_6):
		s += p_5(n - 6 * u - 1)
	return s

if __name__ == "__main__":
	N = int(input("Enter the value of N: "))
	print(p_6(N))