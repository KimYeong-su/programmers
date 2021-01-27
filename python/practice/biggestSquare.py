'''
DP 문제 입니다.. 아이디어는 아래의 사이트를 참고하였습니다.
https://codedrive.tistory.com/53
'''


def solution(board):
    answer = 0
    col = len(board[0])
    row = len(board)
    if col == 1 and row == 1:
        return board[0][0] ** 2
    for i in range(1,row):
        for j in range(1,col):
            if not board[i][j]: continue
            board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
            answer = max(answer,board[i][j])
    return answer**2

print(solution([[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]))
print(solution([[0,0,1,1],[1,1,1,1]]))