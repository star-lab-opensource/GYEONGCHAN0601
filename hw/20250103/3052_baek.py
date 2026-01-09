#3052
numbers=[]
last=[]
for i in range(10):
    a=int(input())
    numbers.append(a)

for j in numbers:
    b=j%42
    last.append(b)
    if b not in numbers:
        last.append(b)

print(len(last))