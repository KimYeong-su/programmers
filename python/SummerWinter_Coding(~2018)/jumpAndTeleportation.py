def solution(n):
    answer = 0
    while 0 < n:
        if n % 2:
            answer += n%2
            n -= n%2
        else:
            n //= 2
    return answer

print(solution(5)) # 2
print(solution(6)) # 2
print(solution(5000)) # 5