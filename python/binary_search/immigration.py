def solution(n, times):
    times.sort()
    maximum = times[0] * n
    minimum = 0
    
    def binary_search(left, right, times, n):
        answer = float('inf')
        while left <= right:
            cnt = 0
            mid = (left+right)//2
            for t in times:
                cnt += mid//t
                
            if cnt >= n:
                answer = min(answer, mid)
                right = mid - 1
            else:
                left = mid + 1
        return answer
    
    return binary_search(minimum, maximum, times, n)

print(solution(6, [7, 10])) # 28