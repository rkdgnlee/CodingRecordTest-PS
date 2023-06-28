def solution(a, b, n):
    answer = 0
    while True:
        answer += (n // a) * b
        n = (n%a) + (n // a) * b
        if n < a:
            break
        elif n == 0:
            break
    return answer