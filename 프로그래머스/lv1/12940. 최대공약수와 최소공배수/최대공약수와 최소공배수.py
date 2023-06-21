def solution(n, m):
    gcd = 1
    lcm = 1
    for i in range(1, m+1):
        if (m % i == 0) and (n % i == 0):
            gcd = i
    
    lcm = int((n * m) /gcd)
    return [gcd, lcm]
        
            
