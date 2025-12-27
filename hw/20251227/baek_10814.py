a=int(input())

list=[]

for i in range(1,a+1):
    age,name= input().split()
    age=int(age)
    order=i
    list.append((age,name,order))


for i in range(len(list)):
    for j in range(i+1, len(list)):
        if list[i][0]>list[j][0]:
            list[i], list[j]=list[j],list[i]

        elif list[i][0]==list[j][0]:
            if list[i][2]>list[j][2]:
                list[i], list[j]=list[j], list[i]

for k in range(len(list)):
    print(list[k][0],list[k][1])

