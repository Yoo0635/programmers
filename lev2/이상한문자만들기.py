def solution1(s):
    result = []
    count = 0
    for x in s:
        if x == " ":
            result.append(" ")
            count = 0
        else:
            if count % 2 ==0:
                result.append(x.upper())
            else:
                result.append(x.lower())
            count += 1
        
    return "".join(result)

def solution2(s):
    return " ".join(map(lambda a: "".join([y.upper() if x % 2 ==0 else y.lower() for x, y in enumerate(a)]) ,s.split()))


print(solution2("try hello world"))