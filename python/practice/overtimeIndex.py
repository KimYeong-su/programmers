import heapq
'''
def solution(n, works):
    works = list(map(lambda x : -x, works))
    while n > 0 and works:
        a = heapq.heappop(works)
        if a == 0: continue
        a += 1
        n -= 1
        heapq.heappush(works, a)
    return sum(map(lambda x: x**2, works))
'''

def solution(n, works):
    heap = []
    for work in works:
        heapq.heappush(heap,-work)
        
    while n > 0 and heap:
        a = heapq.heappop(heap)
        if a == 0: continue
        a += 1
        n -= 1
        heapq.heappush(heap, a)
    return sum(map(lambda x: x**2, heap))

print(solution(4, [4,3,3])) # 12
print(solution(1, [2,1,2])) # 6
print(solution(3, [1,1])) # 0
print(solution(15, [11, 5, 3, 2, 1])) # 11