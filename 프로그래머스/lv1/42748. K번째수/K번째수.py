def solution(array, commands):
    answer = []
    for out in commands:            #command의 n번째 리스
        arr = []
        arr = array[out[0]-1:out[1]]
        arr.sort()
        answer.append(arr[out[2]-1])
    return answer