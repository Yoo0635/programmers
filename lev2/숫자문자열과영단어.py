d = {
        "zero" : "0",
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9
    }
def solution1(s):
    buffer = ""
    result = ""
    for x in s:
        if x.isdigit():
            result += x
        else:
            buffer += x
        print("buffer: " + buffer)
        print("result: " + result)
        if buffer in d:
            result += str(d[buffer])
            buffer = ""

    return int(result)

def solution2(s):
    result = s
    for key, value in d.items():
        result = result.replace(key, value)
    return int(result)



print(solution2("one4seveneight"))