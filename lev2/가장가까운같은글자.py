def solution1(s):
    answer = list(s)
    d = {}
    result = []
    for i in range(len(answer)):
        if answer[i] in d:
            result.append(i-d[answer[i]])
        else:
            result.append(-1)
        d[answer[i]] = i
    return result

def test(s):
    answer = list(s)
    result = []
    d = {}
    for i in range(len(answer)):
        d[answer[i]] = i
        print(d[answer[i]])
    return d

print(solution1("banana"))
# print(test("banana"))