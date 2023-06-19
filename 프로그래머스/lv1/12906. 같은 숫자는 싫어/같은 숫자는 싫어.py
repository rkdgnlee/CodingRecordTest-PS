def solution(arr):
    answer = []
    temp = None
    for i in arr:
        if i != temp:
            answer.append(i)
            temp = i
    return answer
