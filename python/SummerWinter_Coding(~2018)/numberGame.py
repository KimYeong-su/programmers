def solution(A, B):
    answer = 0
    N = len(A)
    A.sort()
    B.sort()
    idx = 0
    for i in range(N):
        if A[idx] < B[i]:
            answer += 1
            idx += 1
    return answer

print(solution([5, 1, 3, 7], [2, 2, 6, 8])) # 3
print(solution([2, 2, 2, 2], [1, 1, 1, 1])) # 0