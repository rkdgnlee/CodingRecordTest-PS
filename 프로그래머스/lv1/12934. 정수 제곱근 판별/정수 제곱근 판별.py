def solution(n):
    nn = n**(1/2)
    if n % nn == 0:
        return (int(nn)+1)**2
    else: 
        return -1