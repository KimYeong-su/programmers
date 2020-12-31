def dfs(idx, result, N, target, numbers):
    global answer
    if idx==N:
        if target == result:
            answer += 1
        return
    dfs(idx+1, result + numbers[idx], N, target, numbers)
    dfs(idx+1, result - numbers[idx], N, target, numbers)
        

def solution(numbers, target):
    global answer
    answer = 0
    N = len(numbers)
    dfs(0, 0, N, target, numbers)
    return answer

print(solution([1,1,1,1,1],3))