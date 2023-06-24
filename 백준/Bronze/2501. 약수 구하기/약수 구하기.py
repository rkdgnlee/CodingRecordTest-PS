a, b = input().split(" ")
a = int(a)
b= int(b)
answer = []
try:
    for n in range(1, a+1):
        if a % n == 0 :
            answer.append(n)

    print(answer[b-1])
except:
    print(0)