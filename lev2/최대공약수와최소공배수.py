def solution2(n, m):
    a, b = max(n, m), min(n, m)
    
    while(b != 0):
        a, b = b, a % b

    return [a, int((n * m) // a)]

def solution(n, m):
    gcd = lambda x, y : y if not x%y else gcd(y, x%y)
    lcm = lambda x, y : (x * y) // gcd(x, y)
    return [gcd(n, m), lcm(n, m)]

print(solution(2, 5))

import math

def solution1(n, m):
    return [math.gcd(n, m), math.lcm(n, m)]