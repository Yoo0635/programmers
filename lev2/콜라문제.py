def solution(a, b, n):
    if n < a:
        return False
    result, buffer = 0, 0
    while(n >= a):
        result += (n // a) * b # 10 * 1 10병 
        buffer = n % a
        n = (n // a) * b + buffer
    return result

def solution2(a, b, n):
    answer = 0
    while n >= a:
        answer += (n // a) * b 
        n = (n // a) * b + (n % a) 
    return answer

print(solution(3,1,20)) # 2개를 주면 1개를 받음 20개 보유 = 19