def solution1(sizes):
    num1, num2 = 0, 0
    for i in range(len(sizes)): # 0, 1, 2, 3
        big = max(sizes[i][0], sizes[i][1])
        small = min(sizes[i][0], sizes[i][1])

        if num1 < big: # 60, 70, 70, 80
            num1 = big
        if num2 < small: # 50, 
            num2 = small
        
    return num1 * num2

def solution2(sizes):
    return max((max(x) for x in sizes)) * max((min(x) for x in sizes))

print(solution2([[60, 50], [30, 70], [60, 30], [80, 40]]))