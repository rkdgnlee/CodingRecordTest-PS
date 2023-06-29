def solution(k, m, score):
    score = sorted(score)
    amount = 0
    while True:
        change = []
        try:
            
            for i in range(0, m):       #m개씩 세고 리스트 change에 담음
                change.append(score[-1])
                score.pop()             #오름차순으로 인덱스 -1값씩 빼면서 
            if len(change) >= m:
                amount += change[-1] * m
            
        except:

            for j in range(0, len(score)):
                change.append(score[-1])
                score.pop() 
            if len(change) < m:
                break       
    return amount