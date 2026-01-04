a, b = map(int, input().strip().split(' '))

for x in range(b):
    for y in range(a):
        print("*" ,end="")
    print()

print("다른 풀이")

answer = ("*" * a + '\n') * b
print(answer)