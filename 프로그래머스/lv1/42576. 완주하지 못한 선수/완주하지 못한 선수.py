def solution(participant, completion):
    try:
        new_p = set(participant)
        new_c = set(completion)
        answer = new_p - new_c
        return list(answer)[0]
    except:
        dict = {}
        for i in range(0, len(participant)):
            if participant[i] not in dict:
                dict[participant[i]] = 1
            elif participant[i] in dict:
                dict[participant[i]] += 1       #명수 추가 하기 끝
        
        for com in completion:
            if com in dict:
                dict[com] -= 1
                if dict[com] == 0:
                    del dict[com]
        
        return list(dict.keys())[0]
            
        
    
    #일단 동명이인없는거 하고 그 다음에 except로
    #딕셔너리로 ㄱ 하는데 인덱스 번호가 아닌 사람 수로 해보기