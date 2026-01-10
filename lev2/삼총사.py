def solution1(number):
    count = 0
    for x in range(len(number)):
        for y in range(x+1, len(number)):
            for z in range(y+1, len(number)):
                if number[x] + number[y] + number[z] == 0:
                    count+=1

    return count

def solution2(number):
    from itertools import combinations
    count = 0
    for i in combinations(number, 3):
        if sum(i) == 0:
            count += 1
    return count

print(solution2([-2, 3, 0, 2, -5]))