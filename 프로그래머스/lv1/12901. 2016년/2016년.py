def solution(a, b):
    day = ["SAT","SUN","MON","TUE","WED","THU","FRI"]
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    count = 0 
    for i in range(0, a-1):
        count += month[i]
    
    count += b # 2016년의 총 일수 다 더해짐
    return day[(count % 7) - 2]
    
    
        
        