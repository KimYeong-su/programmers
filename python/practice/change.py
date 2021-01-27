'''
# 재귀로 풀면 시간초과 납니다. DP로 풀어야 합니다.
def solution(n, money):
    global answer
    answer = 0
    money.sort(reverse=True)

    def exchange(n, money, idx):
        global answer
        if n==0:
            answer += 1
            return
        for i in range(idx, len(money)):
            if money[i] <= n:
                exchange(n-money[i], money, i)
    
    exchange(n,money,0)
    return answer % 1000000007
'''

def solution(n, money):
    dp = [0]*(n+1)
    dp[0] = 1
    for i in range(len(money)):
        for j in range(1,n+1):
            if j >= money[i]:
                dp[j] += dp[j-money[i]]
    return dp[n] % 1000000007

print(solution(5, [1,2,5])) # 4