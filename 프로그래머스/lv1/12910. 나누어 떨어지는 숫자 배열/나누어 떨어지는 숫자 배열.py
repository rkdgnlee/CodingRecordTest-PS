def solution(arr, divisor):
    answer = []
    for ar in arr:
        if ar % divisor == 0:
            answer.append(ar)
        
    if answer == []:
        answer.append(-1)
    answer.sort()
    return answer