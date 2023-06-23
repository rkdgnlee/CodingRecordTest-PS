def solution(seoul):
    answer = ""
    for st in seoul:
        if 'Kim' in st:
            answer = "김서방은 " + str(seoul.index(st)) +"에 있다"
    return answer