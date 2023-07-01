s = input()
s= list(s)
eng = []
for i in range(97, 123):
    eng.append(chr(i))

for i in range(0, len(eng)):
    if eng[i] in s:
        print(s.index(eng[i]), end = " ")
    elif eng[i] not in s:
        print(-1, end= " ")