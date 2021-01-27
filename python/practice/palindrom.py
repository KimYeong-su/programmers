'''
답이 짝수 일때랑 홀수 일때를 나눠서 풀었는데.. 재귀를 써서 돌리면 됐다.. 
def solution(s):
    return len(s) if s[::-1] == s else max(solution(s[:-1]), solution(s[1:]))
'''
def solution(s):
    if len(s)<3:
        return 1
    answer = 1
    n = len(s)
    for i in range(1,n-1):
        for j in range(min(i,n-i-1),0,-1):
            if s[i-j:i+1] == s[i+1:i+2+j][::-1]:
                answer = max(answer, (j+1)*2)
                break
            if s[i-j:i] == s[i+1:i+1+j][::-1]:
                answer = max(answer, j*2+1)
                break      
    return answer

print(solution("abcdcba")) # 7
print(solution("abacde")) # 3
print(solution("abcde")) # 1
print(solution("abba")) # 4