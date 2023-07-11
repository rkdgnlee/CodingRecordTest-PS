logi = input()
# 다이얼 일일 넣어
dial = {}
for i in range(65, 91):
    dial[chr(i)]= 2         #abc
    if i >= 68 and i <= 70:
        dial[chr(i)] = 3    #def
    elif i > 70 and i <= 73: 
        dial[chr(i)] = 4    #ghi
    elif i > 73 and i <= 76:
        dial[chr(i)] = 5    #jkl    
    elif i > 76 and i <= 79:
        dial[chr(i)] = 6    #mno
    elif i > 79 and i <= 83:
        dial[chr(i)] = 7    #pqrs
    elif i > 83 and i <= 86:
        dial[chr(i)] = 8    #tuv
    elif i > 86 and i <= 90:
        dial[chr(i)] = 9    #wxyz
sum = 0
for logg in logi:
    if logg in dial:
        sum += dial.get(logg) + 1
print(sum)