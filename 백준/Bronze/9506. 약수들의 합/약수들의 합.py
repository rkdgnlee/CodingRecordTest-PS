while True:
    a = int(input()) 
    if a == -1:
        break
    sum = 0
    l = []
    for i in range(1, int((a/2) + 1)):
        if a % i == 0:
            sum += i
            l.append(i)
    if sum != a:
        print(a, "is NOT perfect.")
    elif sum == a:
        print(a, end=" = ")
        for j in range(0, len(l)-1): #L-1까지만 하구 + 하고 마지막만 L ㄱ
            print(l[j], end = " + ")
        print(l[-1])