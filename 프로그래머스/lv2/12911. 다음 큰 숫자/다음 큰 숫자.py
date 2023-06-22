def solution(n):
    answer = n
    onecount = bin(n).count("1")
    while True:
        answer += 1
        answercount = bin(answer).count("1")
        if onecount == answercount:
            break
    return answer
        #그 숫자들의 binary해서 count("1")해서 같다. 그러면 break하고 나옴 
        