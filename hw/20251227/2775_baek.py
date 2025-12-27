#2775
t = int(input())
result=[]

for _ in range(t):
    k = int(input())
    n = int(input())

    apart=[]

    for f in range(k+1):
        apart.append([0] * (n+1))

    for r in range(1, n+1):
        apart[0][r] = r

    for f in range(1, k+1):
        for r in range(1, n+1):
            if r == 1:
                apart[f][r] = 1
            else:
                apart[f][r] = (apart[f][r-1] + apart[f-1][r])

    result.append(apart[k][n])


for a in result:
    print(a)