def solution(s, n):
    answer = ''
    for i in s:
        if ord('a') <= ord(i) <= ord('z'):
            answer += chr(ord('a') + (ord(i)-ord('a')+n) % 26)
        elif ord('A') <= ord(i) <= ord('Z'):
            answer += chr(ord('A') + (ord(i)-ord('A')+n) % 26)
        else:
            answer += i
    return answer

print(solution("AB", 1))
print(solution("z", 1))
print(solution("a B z",4))