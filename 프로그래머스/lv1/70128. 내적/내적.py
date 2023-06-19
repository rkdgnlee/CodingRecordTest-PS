def solution(a, b):
    sum = 0
    for i in range(0, len(b)):
        sum += a[i] * b[i]
    return sum