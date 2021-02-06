'''
# https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/
# https://codedoc.tistory.com/95
# 최소 비용문제 이므로 다익스트라나 플로이드 와샬 알고리즘으로 풀면 된다.
# 다익스트라의 경우 최단거리를 바로 구할때 좋지만 이번 문제와 같이 두가지의 최단거리와 중복 거리를 제거해야 하는 경우에는 플로이드 와샬 알고리즘이 훨씬 빠르다.
# 간선의 갯수가 많은 경우에는 다익스트라보다 플로이드 와샬 알고리즘이 좋다.
'''

def solution(n, s, a, b, fares):
    cost = [[float('inf') for _ in range(n)]for _ in range(n)]
    for i in fares:
        u,v,w = i
        cost[u-1][v-1] = min(cost[u-1][v-1], w)
        cost[v-1][u-1] = min(cost[v-1][u-1], w)
        
    for k in range(n):
        cost[k][k] = 0
        for i in range(n):
            for j in range(n):
                if cost[i][j] > cost[i][k]+cost[k][j]: # cost[i][j] = min(cost[i][j], cost[i][k]+cost[k][j])로 표현하는 것 보다 대소비교가 훨씬 빠르다.. 메모..
                    cost[i][j] = cost[i][k]+cost[k][j]
    return min(cost[s-1][k]+cost[k][a-1]+cost[k][b-1] for k in range(n))

print(solution(6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]])) # 82
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])) # 14
print(solution(6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]])) # 18