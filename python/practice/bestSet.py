'''
곱이 가장 크기 위해선 표준편차가 가장 작아야 한다.
따라서 n개의 중앙 값에서 편차 만큼 더해주면 된다.
'''

def solution(n, s):
    answer = [0] * n
    div = s//n
    rest = s%n
    if div:
        for i in range(n):
            answer[i] = div
        for i in range(-rest-1,0,-1):
            print(i)
            answer[i] += 1
        return answer
    else:
        return [-1]

print(solution(2, 9)) # [4,5]
print(solution(2, 1)) # [-1]
print(solution(2, 8)) # [4,4]
print(solution(3, 12)) # [4,4,4]
print(solution(4, 18)) # [4,4,5,5]