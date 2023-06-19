def solution(s):
    if len(s)==4 or len(s)==6:          #s의 길이 
        for ss in s:
            if 48 <= ord(ss) <= 57:
                pass
            else:
                return False            
    else:
        return False
    return True