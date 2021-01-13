from collections import deque
def solution(n, edge):
    v = [0] * n
    m = {}
    for x,y in edge:
        if x in m:
            m[x] += [y]
        else:
            m[x] = [y]
        if y in m:
            m[y] += [x]
        else:
            m[y] = [x]
    queue = deque([1])
    while queue:
        s = queue.popleft()
        try:
            for i in m[s]:
                if v[i-1] or i==1: continue
                v[i-1] = v[s-1] + 1
                queue.append(i)
        except:
            pass
    answer = v.count(max(v))
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))