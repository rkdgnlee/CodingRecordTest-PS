def solution(n):
    nn = sorted(str(n), reverse=True)
    answer = ""
    for i in nn:
        answer += i 
        
    return int(answer)