from p_of_3 import *

def p_4(n):
	q_4 = q(n, 4)
	s = 0
	for u in range(q_4):
		s += p_3(n - 4 * u -1)
	return s

if __name__ == "__main__":
	N = int(input("Enter the value of N: "))
	print(p_4(N))