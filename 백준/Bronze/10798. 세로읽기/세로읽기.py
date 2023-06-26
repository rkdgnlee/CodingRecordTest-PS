s = [input() for i in range(5)]
leng = [len(i) for i in s]
big = max(leng)


for i in range(big):
    for j in range(5):
        try:
            print(s[j][i], end="")
        except:
            continue
