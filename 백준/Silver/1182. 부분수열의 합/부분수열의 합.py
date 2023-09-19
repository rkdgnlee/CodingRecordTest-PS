def back_t(id, res):
    global cnt
    
    # 현재 id가 정수의 개수보다 크거나 같으면 종료
    if id >= len(n_list):
        return
    
    # 수열에 현재 id 정수를 더함
    res += n_list[id]

    # 현재 수열이 s와 일치하면 cnt 증가
    if res == s:
        cnt += 1

    # 현재 id 정수를 더한 경우에 대한 백트래킹
    back_t(id + 1, res)

    # 현재 id 정수를 더하지 않은 경우(백트래킹)
    back_t(id + 1, res - n_list[id])

n, s = map(int, input().split())
n_list = list(map(int, input().split()))
cnt = 0
back_t(0, 0)  # 초기 id와 res를 0으로 시작
print(cnt)