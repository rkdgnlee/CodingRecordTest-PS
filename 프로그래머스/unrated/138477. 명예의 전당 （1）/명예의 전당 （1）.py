def solution(k, score):
    #len(score)  #총 경연 일수
    ranking = []
    answer = []
    for i in range(0, len(score)):   #총 경연 시작 
        if i < k :
            ranking.append(score[i])
            ranking = sorted(ranking, reverse= True)

        elif i >= k :
            ranking.append(score[i])
            ranking = sorted(ranking, reverse = True)
            ranking.pop()
            
        answer.append(ranking[-1])        
    return answer