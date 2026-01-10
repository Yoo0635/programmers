def solution(n):
    
    x = ""
    while n > 0:
        x += str(n % 3)
        n //= 3
    return int(x, 3)
    
print(solution(45))