def solution(arr):
    result = []
    for x in arr:
        if result[-1:] == [x]: 
            continue
        result.append(x)
    return result


def solution2(arr):
    return [arr[i] for i in range(len(arr)) if [arr[i]] != arr[i+1:i+2]]

print(solution2([1,1,3,3,0,1,1]))