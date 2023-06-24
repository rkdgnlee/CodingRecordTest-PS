def solution(N, stages):
    dict = {}
    remain = len(stages)
    for i in range(1, N+1):
        if i in stages:
            dict[i] = stages.count(i) / remain
            remain -= stages.count(i)
        elif i not in stages:
            dict[i] = 0
    l = sorted(dict.items(), key=lambda x:x[1], reverse= True)
    answer = []
    for ll in l:
        answer.append(ll[0])
    return answer
