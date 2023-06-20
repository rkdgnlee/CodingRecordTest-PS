amount = int(input())
n = int(input())
a = []
for i in range(n):
    b =  list(map(int,input().split(" ")))
    a += b
sum = 0
for i in range(0, len(a), 2):
    sum += a[i] * a[i+1]
if amount == sum:
    print("Yes")
else:
    print("No")