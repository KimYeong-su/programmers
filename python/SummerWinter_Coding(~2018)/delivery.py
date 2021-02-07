def solution(N, road, K):
    dp = [[float('inf') for _ in range(N)]for _ in range(N)]
    for r in road:
        u,v,w = r
        dp[u-1][v-1] = min(dp[u-1][v-1], w)
        dp[v-1][u-1] = min(dp[u-1][v-1], w)
    for k in range(N):
        dp[k][k] = 0
        for i in range(N):
            for j in range(N):
                tmp = dp[i][k]+dp[k][j]
                if dp[i][j] > tmp:
                    dp[i][j] = tmp
    return len(list(filter(lambda x : x<=K ,dp[0])))

print(solution(5, [[1, 2, 1], [2, 3, 3], [5, 2, 2], [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3)) # 4
print(solution(6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4)) # 4