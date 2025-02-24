# Yet to implement as of epoch @1737992903
"""
Citation:
  #1 :: https://www.youtube.com/watch?v=iJ8pnCO0nTY
  #2 :: https://oeis.org/A001318
  #3 :: https://en.wikipedia.org/wiki/Pentagonal_number_theorem
  #4 :: https://pages.uoregon.edu/koch/PentagonalNumbers.pdf
  
  NOTE: The video lecture by Dr. Burkard Polster on his YouTube channel, Mathologer, was instrumental in inspiring this algorithm. 
  The implementation below is intended to demonstrate what he referred to as the "Euler-chain-engine," rather than simply solving 
  the problem using Pentagonal Numbers or related concepts.
  
  I would also like to emphasize that, while Dr. Burkard's explanations and animations make the algorithm easy to understand, 
  coders are encouraged to pay close attention to the memory consumption of their machines when implementing this solution.

Thanks,  
Darshan P.
Commit@1737993021
"""

# Human:
# Partition of N(say100) then you have to set BREAK_POINT=101

# Computers:
# Partition of N(say100) then you have to find the value of 100th Index of ColVect

# len(ColVect) = BREAK_POINT
# Therefore, BREAK_POINT = N+1 ( Where: N = Partition you are trying to find )

N=int(input("Enter the value of N for the partition(N): "))
# SET THE VALUE OF PARTITION YOU WANT TO FIND
BREAK_POINT = N+1
def mult(r, c):
    c.append(sum(r[i]*c[i] for i in range(len(r))))
colvect = [1]
rowvect = []
n, p = 1, 1
k = 1
pent = lambda x: x * ( 3 * x - 1 ) // 2

# Here, as per the Mathologer video, I wanted to try generating pentagonal numbers using 
# N_natural and N_odd. However, I didn't want to spend time on that for some reason. 
# Contributions and comments are welcome.

while True:
    pos_neg = 0
    if n == pent(k*p):
        if p % 2 == 0:
            pos_neg = -1
        else:
            pos_neg = 1
        if k == 1 :
            k = -1
        else:
            k = 1
            p += 1
    rowvect.insert(0, pos_neg)
    n += 1
    mult(rowvect, colvect)
    if n == BREAK_POINT:
        break
#print("colVect", colvect)
print(colvect[N])


```
# I'm so glad I finally tried this! It had been on my reminders list for the past 4-5 weeks, 
# and I'm incredibly happy that I gave it a shot.
# It however fails to compete with sympy.partitions
>>> from sympy import *; partition(100)
190569292


[Ilya@m87 partalgo]$ python3 euler_gen.py 
Enter the value of N for the partition(N): 100
190569292
[Ilya@m87 partalgo]$ python3 euler_gen.py 
Enter the value of N for the partition(N): 6660
176391179771416981710569585813452498508987474057399720269827317078498698483361307187738
[Ilya@m87 partalgo]$ python3 euler_gen.py 
Enter the value of N for the partition(N): 1000
24061467864032622473692149727991
[Ilya@m87 partalgo]$ cat euler_gen.py | pbcopy 
[Ilya@m87 partalgo]$ python3 euler_gen.py 
Enter the value of N for the partition(N): 9999
35709901879704736738758549207052696680819022123397567612860179055188265961723158018938110612668644192313000
[Ilya@m87 partalgo]$ python3 euler_gen.py 
Enter the value of N for the partition(N): 9999
35709901879704736738758549207052696680819022123397567612860179055188265961723158018938110612668644192313000
[Ilya@m87 partalgo]$ 
```


