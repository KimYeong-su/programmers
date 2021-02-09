def solution(d, budget):
    d.sort()
    for i in range(len(d)):
        if sum(d[:i+1]) > budget:
            return i
    else:
        return i+1

print(solution([1, 3, 2, 5, 4], 9)) # 3
print(solution([2, 2, 3, 3], 10)) # 4