def solution(absolutes, signs):
    sum = 0
    for i in range(0, len(signs)):
        if signs[i] == True:
            sum += absolutes[i] 
        elif signs[i] == False:
            sum -= absolutes[i]
    return sum
