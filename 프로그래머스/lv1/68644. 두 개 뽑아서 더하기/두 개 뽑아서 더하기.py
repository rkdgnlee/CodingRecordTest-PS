def solution(numbers):
    answer = []
    answer_set = set()
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)): 
            answer_set.add(numbers[i] + numbers[j])
            
    answer = list(answer_set)
    answer.sort()
    
    return answer