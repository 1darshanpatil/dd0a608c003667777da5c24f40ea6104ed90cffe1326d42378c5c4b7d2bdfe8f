from math import floor

q = lambda n, k : n // k


def p_3(n):
	q_3 = q(n, 3)
	s = 0
	for i in range(1, q_3 + 1):
		s += q(n - i, 2) - (i - 1)
	return s

if __name__ == "__main__":
	n = int(input("Enter the value of N: "))
	print(p_3(n))