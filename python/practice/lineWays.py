def solution(n, k):
    def factorial(n):
        if n==1:
            return n
        return n*factorial(n-1)
    answer = []
    number = [i for i in range(1,n+1)]
    while n != 0:
        tmp = factorial(n) // n
        index = k // tmp
        k = k % tmp
        if k == 0:
            answer.append(number.pop(index-1))
        else:
            answer.append(number.pop(index))
        n -= 1
    return answer

print(solution(3,5)) # [3,1,2]
print(solution(4,14)) # [3, 1, 4, 2]