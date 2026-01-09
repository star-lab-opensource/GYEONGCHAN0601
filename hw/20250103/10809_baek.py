#10809
a = input()

alphabet = "abcdefghijklmnopqrstuvwxyz"
final = []


for i in range(len(alphabet)):
    number=-1
    for j in range(len(a)):
        if alphabet[i]==a[j]:
            number = j
            break
    final.append(number)
    
    

    
print(*final)