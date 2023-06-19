def solution(n):
    answer = ""
    if n == 1:
        return 1
    else:
        while n > 1:
            answer += str(n % 3)
            n = n // 3
            if n == 1:
                answer += str(n)
                break
        return int(answer, 3)