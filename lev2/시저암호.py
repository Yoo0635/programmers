def solution(s, n):
    answer = []
    for x in s:
        if x == ' ':
            answer.append(' ')
        elif x.isupper():
            answer.append(
                chr((ord(x) - ord('A') + n) % 26 + ord('A'))
            )
        elif x.islower():
            answer.append(
                chr((ord(x) - ord('a') + n) % 26 + ord('a'))
            )
        else:
            answer.append(x)

    return "".join(answer)


print(solution("a B z", 4))   # e F d
print(solution("abcd", 1))    # bcde
