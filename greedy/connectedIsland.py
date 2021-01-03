import heapq
def find(n, visit):
    if visit[n] == n:
        return n
    return find(visit[n], visit)

def union(x, y, visit, rank):
    a = find(x, visit)
    b = find(y, visit)
    if rank[a] > rank[b]:
        visit[b] = a
    else:
        visit[a] = b
        if rank[a] == rank[b]:
            rank[a] += 1
    

def solution(n, costs):
    answer = 0
    heap = []
    for c in costs:
        heapq.heappush(heap, (c[2], c[0], c[1]))
    visit = [x for x in range(n)]
    rank = [0] * n
    while heap:
        c, x, y = heapq.heappop(heap)
        if find(x, visit) != find(y, visit):
            union(x,y,visit,rank)
            answer += c
    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]))