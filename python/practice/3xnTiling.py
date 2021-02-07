'''
# 이해하기가 너무 어렵네요..
# 짝수 밖에 안되고 특수한 경우가 계속해서 추가되는 것을 생각해보면 됩니다.
# 기본적으로 두칸에서 가능한 갯수가 3가지 이므로 3을 계속해서 곱해가면 중간에 가로 두개가 들어가는 특수한 케이스에서는 2개씩 증가하는 것과 전체에서 2개가 증가하는 경우를 생각해야한다.
# https://wonillism.github.io/programmers/Programmers-3xn-tiling/
'''

def solution(n):
    answer = [0,3,11]
    index = n//2
    if n % 2 != 0: return 0
    if index < 3: return answer[index]
    
    for i in range(3, index+1):
        answer.append((3*answer[i-1] + sum(answer[1:i-1])*2 + 2)%1000000007)
    return answer[index]

print(solution(2)) # 3
print(solution(4)) # 11
print(solution(6)) # 41