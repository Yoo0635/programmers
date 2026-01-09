def solution(d, budget):
    
    result = 0
    d.sort()
    for x in d:
        if budget < x:
            break
        budget -= x
        result += 1
    return result
print(solution([2,2,3,3], 10))