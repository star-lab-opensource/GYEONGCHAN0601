#1676
import math


n=int(input())

n_factorial=math.factorial(n)

str_n=str(n_factorial)

one=0

for i in range(len(str_n)-1, 0, -1):                 
    if str_n[i]=="0":
        one+=1

    else:
        break

print(one)
