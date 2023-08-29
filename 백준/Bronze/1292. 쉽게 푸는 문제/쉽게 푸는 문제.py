num_list = []
start = 1
while len(num_list) <= 1000:
    for i in range(1, start+1):
        num_list.append(start)
    start += 1
a, b = input().split(" ")
a = int(a)
b = int(b)

sum = 0
for i in num_list[a-1:b]:
    sum += i
print(sum)