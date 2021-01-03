def divide(node, base):
    w = []
    l = []
    for i in range(len(base[node])):
        if base[node][i] == 1:
            w.append(i)
        elif base[node][i] == -1:
            l.append(i)
    return w, l

def solution(n, results):
    answer = 0
    base = [[0 for _ in range(n)] for _ in range(n)]
    cnt = {}
    for i, j in results:
        base[i-1][j-1] = 1
        base[j-1][i-1] = -1
        if i-1 in cnt:
            cnt[i-1] += 1
        else:
            cnt[i-1] = 1
        if j-1 in cnt:
            cnt[j-1] += 1
        else:
            cnt[j-1] = 1
    cnt = sorted(cnt.items(), key = lambda x : -x[1])
    for idx, _ in cnt:
        win,lose = divide(idx, base)
        for i in win:
            for j in lose:
                base[j][i] = 1
                base[i][j] = -1
    for i in base:
        if i.count(0) == 1:
            answer += 1
            
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))