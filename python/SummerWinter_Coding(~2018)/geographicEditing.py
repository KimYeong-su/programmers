'''
# https://deok2kim.tistory.com/126
# 아예 없애고 1층씩 만들어가면서 최소값을 찾아간다.
# 증가하기 시작하면 멈추기
'''
def solution(land, P, Q):
    base = []
    for l in land:
        base+=l
    base.sort()
    n = len(base)
    cost = (sum(base) - base[0]*n) * Q
    answer = cost
    for i in range(1,n):
        if base[i] != base[i-1]:
            cost = cost + ((base[i] - base[i-1]) * i * P) - ((base[i] - base[i-1])*(n-i) * Q)
            if answer < cost:
                break
            answer = min(answer, cost)
    return answer

print(solution([[1, 2], [2, 3]], 3, 2)) # 5
print(solution([[4, 4, 3], [3, 2, 2], [2, 1, 0]], 5, 3)) # 33