def solution(numbers):
    result = []

    for x in range(len(numbers)):
        for y in range(x+1, len(numbers)):
            if numbers[x] + numbers[y] not in result:
                result.append(numbers[x] + numbers[y])
    result.sort()
    return result

print(solution([2,1,3,4,1]))