def solution(n):
    sequence = [0, 1]
    for i in range(2, n+1):
        sequence.append(sequence[i-1]+sequence[i-2])
    return sequence[n] % 1234567
# 0 1 1 2 3 5 8 13