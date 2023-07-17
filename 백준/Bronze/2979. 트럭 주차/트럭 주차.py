fee_list = list(map(int, input().split(" ")))
fee = 0
dayy = {}
# 3번 입력받으며 그 범위만큼  dayy딕셔너리에 +1씩 하기
for i in range(3):
    a, b = map(int, input().split(" "))
    for j in range(a, b):
        if j not in dayy:
            dayy[j] = 1
        elif j in dayy:
            dayy[j] += 1
# chart = 총 일수 별/ 겹치는 부분은 3  
chart = list(dayy.values())

for k in range(0, len(fee_list)):
    if k >= 1:
        fee += fee_list[k] * chart.count(k+1) * (k+1)
    else:
        fee += fee_list[k] * chart.count(k+1)
    
print(fee)