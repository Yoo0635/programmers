def solution(food):
    copy1 = []
    copy2 = []
    result = []

    for x in range(1, len(food)):
        copy1 += [x] * (food[x] // 2) 
        copy2 += [x] * (food[x] // 2) 
        
    copy1.append(0)
    copy2 = sorted(copy2, reverse=True)
    result = copy1 + copy2

    return "".join(map(str, result))

print(solution([1, 3, 4, 6]))