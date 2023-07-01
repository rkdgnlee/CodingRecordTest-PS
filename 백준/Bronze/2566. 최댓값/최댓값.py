arr= []
for i in range(9):
    arr.append(list(map(int, input().split(" "))))
                   #여기까지 다 잘들어감. 
win = []
for ar in arr: #배열의 첫행에 한번씩 
    win.append(max(ar))
print(max(win))

for ar in arr:
    if max(win) in ar:
        print(arr.index(ar) + 1, ar.index(max(win)) + 1)
