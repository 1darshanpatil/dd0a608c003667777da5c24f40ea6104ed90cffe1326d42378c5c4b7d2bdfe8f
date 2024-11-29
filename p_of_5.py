from p_of_4 import *

def p_5(n):
	q_5 = q(n, 5)
	s = 0
	for u in range(q_5+1):
		s += p_4(n - 5 * u - 1)
	return s

if __name__ == "__main__":
	N = int(input("Enter the value of N: "))
	print(p_5(N))