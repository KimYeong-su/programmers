def solution(n, computers):
    def getParent(cycle,x):
        if cycle[x]==x: return x
        return getParent(cycle, cycle[x])
    answer = 0
    cycle = [x for x in range(n)]
    for i in range(n):
        for j in range(n):
            if i==j: continue
            if not computers[i][j]: continue
            if getParent(cycle, i) == getParent(cycle, j): continue
            tmp1 = min(getParent(cycle,i), getParent(cycle,j))
            if cycle[i] == min(getParent(cycle,i), getParent(cycle,j)):
                tmp = cycle[j]
                cycle[j] = tmp1
                for c in range(n):
                    if cycle[c] == tmp:
                        cycle[c] = tmp1
            else:
                tmp = cycle[i]
                cycle[i] = tmp1
                for c in range(n):
                    if cycle[c] == tmp:
                        cycle[c] = tmp1
    answer = len(set(cycle))
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))