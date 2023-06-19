def solution(n):
    if n % 2 == 0:
        return "수박" * int(n//2)
    elif n % 2 == 1:
        return ("수박" * int(n // 2)) + "수"