def solution(s):
    answer = ''
    my_list = list(s)
    my_list.sort(reverse=True)
    for i in my_list:
        answer += i
    return answer