def solution(s):
    count1 = 0
    count2 = 0
    
    for i in range(len(s)):
        if (s != "1") and ("0" in s):
            count2 += s.count("0")
            s = s.replace("0", "")
        elif (s != "1"):
            pass
        elif (s == "1"):
            break
            
        if s != "1":
            s = bin(len(s))
            s = s[2:]
            
        else:
            count1 += 1
            break
        count1 += 1
    return [count1, count2]