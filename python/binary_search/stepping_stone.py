def solution(distance, rocks, n):
    maximum = distance
    minimum = 0
    rocks.sort()
    rocks.append(distance)
    
    def binary_search(left, right, rocks, n):
        answer = 0
        while left <= right:
            cnt = 0
            prev = 0
            mid = (left+right) // 2
            mini = float('inf')
            
            for r in rocks:
                if r-prev < mid:
                    cnt += 1
                else:
                    mini = min(mini, r-prev)
                    prev = r
            if cnt > n:
                right = mid - 1
            else:
                answer = max(answer,mini)
                left = mid + 1
        return answer
            
    return binary_search(minimum, maximum, rocks, n)

print(solution(25, [2, 14, 11, 21, 17], 2)) # 4