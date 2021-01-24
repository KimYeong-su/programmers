'''
이 문제는 모든게 열,행 순으로 주어집니다.
'''

def solution(m, n, puddles):
    board = [[0 for _ in range(m)]for _ in range(n)]
    board[0][0] = 1
    visit = [[False for _ in range(m)]for _ in range(n)]
    visit[0][0] = True
    
    for p in puddles:
        y,x = p
        visit[x-1][y-1] = True
        
    dx = [0,1]
    dy = [1,0]
    queue = [(0,0)]
    
    while queue:
        x,y = queue.pop(0)
        
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
                if 0<=nx-1:
                    board[nx][ny] += board[nx-1][ny]
                if 0<=ny-1:
                    board[nx][ny] += board[nx][ny-1]
                queue.append((nx,ny))
                visit[nx][ny] = True
    return board[n-1][m-1] % 1000000007

print(solution(4,3,[[2,2]]))