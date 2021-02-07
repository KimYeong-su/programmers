import math

def solution(n, stations, w):
    answer = 0
    if stations[0]-w > 0:
        answer += math.ceil((stations[0]-w-1)/(2*w+1))
    end = stations[0]+w
    stations.pop(0)
    while stations:
        s = stations.pop(0)
        start = s-w
        if start<n:
            answer += math.ceil((start-end-1)/(2*w+1))
            end = s+w
    if n-end > 0:
        answer += math.ceil((n-end)/(2*w+1))
    return answer

print(solution(11, [4, 11], 1)) # 3
print(solution(	16, [9], 2)) # 3