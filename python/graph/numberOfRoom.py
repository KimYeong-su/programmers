
'''
# https://www.leejg.me/algorithm-test/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EA%B3%A0%EB%93%9D%EC%A0%90-kit-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%ED%92%80%EC%9D%B4/3-%EB%B0%A9%EC%9D%98-%EA%B0%9C%EC%88%98
# 처음 코드는 노드만 이용하여 알고리즘을 구현했지만, 반복되는 모양이나 대각선 두개를 이용하여 방이 만들어 질 수 있다는 경우를 간과했다.
# 이를 해결하기 위해 2번의 이동과 엣지의 방향을 저장하여 중복확인을 해줬다.
'''
from collections import defaultdict

def solution(arrows):
    answer = 0
    dx = [-1,-1,0,1,1,1,0,-1]
    dy = [0,1,1,1,0,-1,-1,-1]
    x,y = 0, 0
    visit = set([(0,0)])
    edges = defaultdict(int)
    for i in arrows:
        for _ in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx, ny) in visit and edges[(x,y,nx,ny)] == 0:
                answer+= 1
            edges[(x,y,nx,ny)] += 1
            edges[(nx,ny,x,y)] += 1
            visit.add((nx,ny))
            x = nx
            y = ny
    return answer

print(solution(	[6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0])) # 3
print(solution(	[6, 0, 3, 0, 5, 2, 6, 0, 3, 0, 5])) # 3