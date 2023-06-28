def solution(name, yearning, photo):
    dictt = {}
    score = 0
    answer = []
    for i in range(0, len(name)):
        dictt[name[i]] = yearning[i] #딕셔너리에 그리움 점수 다 담김
    
    for ph in photo:
        score = 0
        for i in range(0, len(ph)): #photo 첫 장의 사람 명수 for문
            if ph[i] in dictt:
                score += dictt[ph[i]]
        answer.append(score)
    
    return answer