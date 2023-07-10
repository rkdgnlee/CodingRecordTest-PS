

n = int(input())
for i in range(n):
    one = []
    a = int(input())
    
    if a // 25 >= 1:
        one.append(a//25)
    elif a // 25 == 0:
        one.append(0)
    
    if (a % 25) // 10 >= 1:
        one.append((a % 25) // 10)
    elif (a % 25) // 10 == 0:
        one.append(0)
        
    if ((a % 25) % 10) // 5 == 0 :
        one.append(0)
    elif ((a % 25) % 10) // 5 >= 1:
        one.append(((a % 25) % 10) // 5)
    
    one.append(((a % 25) % 10) % 5)
    print(one[0], one[1], one[2], one[3])