def solution(s):
    num_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num_dict = {}
    for i in range(0, 10):
        num_dict[num_list[i]] = i
    
    for num_eng in num_list:
        if num_eng in s:
           s =  s.replace(num_eng, str(num_dict.get(num_eng)))
    return int(s)
    
    