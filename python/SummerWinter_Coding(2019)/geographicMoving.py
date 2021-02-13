def solution(land, height):
    answer = 0
    N = len(land)
    visit = [[0 for _ in range(N)]for _ in range(N)]
    case = []
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    cnt = 1
    for i in range(N):
        for j in range(N):
            if visit[i][j]!=0: continue
            visit[i][j] = cnt
            queue = [(i,j)]
            while queue:
                x,y = queue.pop(0)
                for k in range(4):
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if 0<=nx<N and 0<=ny<N and visit[nx][ny]==0:
                        if abs(land[x][y]-land[nx][ny]) <= height:
                            visit[nx][ny] = cnt
                            queue.append((nx,ny))
                        else:
                            case.append((abs(land[x][y] - land[nx][ny]),x,y,nx,ny))
            cnt += 1
    case.sort()
    check = [x for x in range(cnt-1)]
    rank = [0 for _ in range(cnt-1)]
    def find(idx, check):
        if check[idx] == idx:
            return idx
        return find(check[idx],check)
    def union(idx1, idx2, check, rank):
        root1 = find(idx1, check)
        root2 = find(idx2, check)
        
        if root1 != root2:
            if rank[root1] > rank[root2]:
                check[root2] = root1
            else:
                check[root1] = root2
                if rank[root1] ==  rank[root2]:
                    rank[root2] +=1
    
    for c in case:
        w, x, y, nx, ny = c
        idx1 = visit[x][y] - 1
        idx2 = visit[nx][ny] - 1
        if find(idx1,check) != find(idx2,check):
            union(idx1, idx2, check, rank)
            answer += w
    
    return answer

print(solution([[1, 4, 8, 10], [5, 5, 5, 5], [10, 10, 10, 10], [10, 10, 10, 20]], 3)) # 15
print(solution([[10, 11, 10, 11], [2, 21, 20, 10], [1, 20, 21, 11], [2, 1, 2, 1]], 1)) # 18