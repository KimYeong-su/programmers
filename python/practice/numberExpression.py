'''
# (해설) 초항 a이고 공차 1 인 n개의 등차 수열의 합이라고 본다.

Sn = n(2*a + (n-1))/2가 되는데

i) n이 홀수 이면 (2*a + (n-1)) 는 짝수 이고

ii) n이 짝수 이면 (2*a - (n-1)) 는 홀수 이다.

쉽게 생각하면 Sn = (홀수 * 짝수)/2 이고 나누기 2는 짝수에 따라 홀수가 될수도 있고 짝수가 될 수 도 있으므로 홀수는 무조건 있다.

따라서, n을 나눌 수 있는 홀수의 갯수와 연속된 숫자의 경우의 수가 같다.


def solution(num):
    answer = [i  for i in range(1,num+1,2) if num % i == 0]
    print(answer)
    return len(answer)
'''
def solution(n):
    answer = 0
    for i in range(1,n+1):
        for j in range(i, 0, -1):
            if (i*(i+1) - j*(j-1)) > 20000: break
            if (i*(i+1) - j*(j-1)) == 2 * n:
                answer += 1
    return answer

print(solution(15)) # 4
print(solution(14)) # 2
print(solution(2)) # 1