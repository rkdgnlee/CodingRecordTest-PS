def solution(A,B):
    #첫 최솟값
    A.sort()
    B.sort()
    length = len(A)
    sum = 0 
    sum += A[0] * B[-1]
    for i in range(1, length):
        sum += A[i] * B[-(i+1)]
    return sum