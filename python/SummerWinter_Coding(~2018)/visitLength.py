def solution(dirs):
    answer = 0
    dd = {'U':0, 'D':1, 'R':2, 'L':3}
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]
    points = []
    x,y = 0,0
    for d in dirs:
        idx = dd[d]
        nx = x + dx[idx]
        ny = y + dy[idx]
        if -6 < nx < 6 and -6 < ny < 6:
            if (x,y,nx,ny) not in points and (nx,ny,x,y) not in points:
                points.append((x,y,nx,ny))
                points.append((nx,ny,x,y))
                answer+=1
            x = nx
            y = ny
    return answer

print(solution("ULURRDLLU")) # 7
print(solution("LULLLLLLU")) # 7