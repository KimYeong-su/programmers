'''
# 다른 사람들은 카탈란 수로 풀었습니다.
# https://soccer-programming.tistory.com/18
from math import factorial
def parenthesisCase(n):
    return factorial(2*n)//(factorial(n)*factorial(n)*(n+1))
'''
def dfs(n,result,stack,cnt1, cnt2, case):
    global answer
    if cnt1 == cnt2 == n and not stack:
        answer.add(result)
        return
    for i in range(2):
        if case[i] == '(':
            if cnt1 < n:
                dfs(n,result+case[i],stack+[case[i]],cnt1+1,cnt2,case)
        else:
            if stack and stack[-1] == '(' and cnt2 < n:
                dfs(n,result+case[i],stack[0:len(stack)-1],cnt1,cnt2+1,case)

def solution(n):
    global answer
    answer = set()
    case = ['(',')']
                   
    dfs(n,'(',['('],1,0, case)
    
    return len(answer)

print(solution(2))
print(solution(3))
