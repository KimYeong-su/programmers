from itertools import combinations
def solution(nums):
    answer = 0
    cases = list(combinations(nums,3))
    for case in cases:
        num = sum(case)
        for i in range(2,int(num**0.5)+1):
            if num % i == 0:break
        else:
            answer += 1
    return answer

print(solution([1,2,3,4])) # 1
print(solution([1,2,7,6,4])) # 4