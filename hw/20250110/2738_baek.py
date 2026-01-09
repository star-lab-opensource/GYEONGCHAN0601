#2738
n,m= map(int, input() .split())

a=[]

for i in range(n):
    A1= list(map(int, input().split()))
    a.append(A1)


b=[]

for i in range(n):
    B1= list(map(int, input().split()))
    b.append(B1)




last=[]

for i in range(n):
    last1=[]
    for j in range(m):
        last1.append(a[i][j]+b[i][j])
    last.append(last1)


for last1 in last:
    print(*last1)