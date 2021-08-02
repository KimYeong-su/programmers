'''
# https://walwal234.tistory.com/37
# visit 함수 대신 문자열을 이용하여 방문 정보를 사용했다는 점이 대단합니다.
# 그렇게 해서 가장 먼저 모든 카드를 찾는 방법을 찾았습니다.
# bfs 경우 모든 경우를 병행해서 진행하다보니 가능한 방법
# list 보다 확실히 deque를 사용하는 것이 훨씬 빠릅니다.
'''

from collections import deque

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def end_game(b):
    if b.count("0") == 16:
        return True
    return False

def remove_element(b, e):
    b = b.replace(e, "0")
    return b

def move(b, y, x, dy, dx):
    ny, nx = y + dy, x + dx
    if 0 <= ny < 4 and 0 <= nx < 4 and b[ny * 4 + nx] == "0":
        return move(b, ny, nx, dy, dx)
    else:
        if 0 <= ny < 4 and 0 <= nx < 4:
            return (ny, nx)
        else:
            return (y, x)

def solution(board, r, c):
    answer = 0
    b = ""
    for i in range(4):
        for j in range(4):
            b += str(board[i][j])
    q = deque([])

    cnt = 0
    enter = -1 # enter을 클릭했던 위치
    q.append((r, c, b, cnt, enter))
    s = set()

    while q:
        y, x, b, c, e = q.popleft()
        pos = 4 * y + x

        if (y, x, b, e) in s:
            continue
        s.add((y, x, b, e))

        if end_game(b):
            return c

        # 4 방향 이동
        for (dy, dx) in d:
            ny, nx = y + dy, x + dx
            if ny >= 0 and ny < 4 and nx >= 0 and nx < 4:
                q.append((ny, nx, b, c+1, e))

        # Ctrl + 4 방향 이동
        for (dy, dx) in d:
            ny, nx = move(b, y, x, dy, dx)
            if ny == y and nx == x:
                continue
            q.append((ny, nx, b, c+1, e))

        # enter를 하는 경우
        if b[pos] != 0:
            if e == -1:
                n_e = pos
                q.append((y, x, b, c+1, n_e))
            else:
                if e != pos and b[e] == b[pos]:
                    b = remove_element(b, b[e])
                    q.append((y, x, b, c+1, -1))

    return answer