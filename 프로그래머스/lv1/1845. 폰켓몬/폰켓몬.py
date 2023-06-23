def solution(nums):
    dict = {}
    choose = len(nums) / 2
    for num in nums:
        if num not in dict:
            dict[num] = 1
        elif num in dict:
            dict[num] += 1
            
    if len(dict) > choose:
        return choose
    elif len(dict) < choose:
        return len(dict)
    else:
        return choose
        
        
        
        
        #번호: 갯수 로 넣기 len(dict)는 포켓몬 종 종 개수임 
        #nums/2는 뽑는 갯수 
        #[1, 2, 3, 4, 5, 6] 개수 6 뽑기는 3 이니 3 
        #[1, 1, 2, 2, 4, 5] 개수 4 뽑기 3
        #[2, 2, 2, 3, 3, 3, 3, 3, 5, 5, 1, 1] 개수 4 뽑기 6  가지수 4 