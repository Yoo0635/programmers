def solution1(array, commands):
    buffer = []
    result = []

    for x in commands:
        buffer = array[x[0]-1: x[1]]
        buffer = sorted(buffer)
        result.append(buffer[x[2] - 1])
        print(buffer)
    return result

def solution2(array, commands):
    return list(map(lambda x: sorted(array[x[0]-1 : x[1]]) [x[2] -1], commands))
    


print(solution2([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))