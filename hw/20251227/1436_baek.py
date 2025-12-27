#1436
n=int(input())

count=0
death_number=666

while count != n:
    str_death_number=str(death_number)

    if "666" in str_death_number:
        count+=1

    if count == n:
        break

    death_number+=1



print(death_number)
