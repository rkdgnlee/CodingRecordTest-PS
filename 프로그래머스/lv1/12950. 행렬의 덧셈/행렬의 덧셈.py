def solution(arr1, arr2):
    answer = []
    a = []
    for i in range(len(arr1)):  #바깥쪽 큰 배열 0, 1
        for j in range(len(arr1[0])): #안쪽 작은 배열 0~1
            a.append(arr1[i][j]+arr2[i][j])
        answer.append(a)
        a= []
    return answer