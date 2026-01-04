def solution(t, p):
    result = 0
    for x in range(len(t) - len(p) + 1):
        if int(p) >= int(t[x: x + len(p)]):
            result += 1
    return result

def solution1(t, p):
    return len([t[i: i+len(p)] for i in range(len(t)-len(p)+1) if int(t[i: i+len(p)]) <= int(p)])

print(solution("500220839878", "7"))