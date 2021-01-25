'''
# (해설) num = n * m이라고 가정합시다.
# (n은 홀수) 이때 num이 연속된 자연수의 합으로 표현되는 방식은 다음과 같이 두 가지 방법이 있습니다.

# i)	중간 숫자가 m이고 연속된 n개의 자연수를 더하는 경우 : 이때 자연수의 합은 m-(n-1)/2 ~ m+(n-1)/2까지이며 이것이 올바른 합이 되려면 m-(n-1)/2 > 0. 즉 n<2m+1을 만족해야 합니다.

# ii)	중간 두 개의 숫자가 (n-1)/2, (n+1)/2이고 연속된 2m개의 자연수를 더하는 경우 : 이때 자연수의 합은 (n-1)/2-(m-1) ~ (n+1)/2+(m-1)이며 이것이 올바른 합이 되려면 (n-1)/2-(m-1) > 0. 즉 n > 2m-1을 만족해야 합니다.

# iii)	n은 홀수이므로 n < 2m+1과 n > 2m-1을 동시에 만족할 수 없고 동시에 어떤 m, n에 대해서도 두 조건 중 하나는 반드시 만족하게 됩니다. (중복 되는 경우는 없다)

# 결론적으로 num = n*m을 만족하는 홀수 n과 연속된 자연수의 합은 일대일 대응을 만족하고 그 개수가 같게 됩니다.


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