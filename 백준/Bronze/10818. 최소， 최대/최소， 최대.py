N= input()
n_list=list(map(int,input().split(" ")))

for i in range(0, len(n_list)):
    n_list[i] = int(n_list[i])
print(min(n_list), max(n_list))
