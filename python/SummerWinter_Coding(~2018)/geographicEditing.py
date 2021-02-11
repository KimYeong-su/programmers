'''

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