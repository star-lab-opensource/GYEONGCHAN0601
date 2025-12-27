#2563

n=int(input())

paper=[]

for i in range(100):
    r=[0]*100
    paper.append(r)


for i in range(n):
    x,y=map(int, input().split())


    for j in range(x, x+10):
        for k in range(y, y+10):
            paper[j][k]=1


result=0

for f in range(100):
    for m in range(100):
        if paper[f][m]==1:
            result+=1       
        

print(result)