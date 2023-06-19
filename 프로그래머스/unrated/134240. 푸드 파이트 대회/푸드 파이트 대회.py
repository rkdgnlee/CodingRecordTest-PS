def solution(food):
    answer = ""
    answer_rev = ""
    for i in range(1, len(food)):       #1~4리스트
        if food[i] == 1:
            pass
        else:
            count = 0
            for j in range(0, food[i] // 2):
                answer = answer + str(i)
                answer_rev = str(i) + answer_rev
                count += j
                
    return answer + "0" + answer_rev  
