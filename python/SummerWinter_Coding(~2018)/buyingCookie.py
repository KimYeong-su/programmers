'''
# accumulate 라는 누적함수가 있습니다.
from itertools import accumulate

def solution(cookie):
    answer = 0
    for m in range(len(cookie)-1):
        a = set(accumulate(reversed(cookie[:m+1])))
        b = set(accumulate(cookie[m+1:]))
        c = a & b

        if c:
            answer = max(*c, answer)
    return answer
'''

'''
# 한쪽의 누적 된 수들을 모아 두고 다른쪽을 검사하면서 겹치는 숫자중에 maximum을 찾아갑니다.
def solution(cookie):
    largest = set()
    for m in range(1, len(cookie)):
        lsum = 0
        rsum = 0
        lsums = set()
        for i in range(m-1, -1, -1):
            lsum += cookie[i]
            lsums.add(lsum)
        for j in range(m, len(cookie)):
            rsum += cookie[j]
            if rsum in lsums:
                largest.add(rsum)
    return max(largest) if largest else 0
'''

def solution(cookie):
    answer = 0
    N = len(cookie)
    for m in range(N-1):
        tmp_a = cookie[m]
        tmp_b = cookie[m+1]
        
        i = 1
        j = 1
        while m-i >= 0 or m+1+j < N:
            if tmp_a == tmp_b:
                if answer < tmp_a:
                    answer = tmp_a
                if m-i >= 0 and m+1+j < N:
                    tmp_a += cookie[m-i]
                    i += 1
                    tmp_b += cookie[m+1+j]
                    j += 1
                else:
                    break
            elif tmp_a < tmp_b:
                if m-i >= 0:
                    tmp_a += cookie[m-i]
                    i += 1
                else:
                    break
            else:
                if m+1+j < N:
                    tmp_b += cookie[m+1+j]
                    j += 1
                else:
                    break
        if tmp_a == tmp_b:
            if answer < tmp_a:
                answer = tmp_a

    return answer

print(solution([1,1,2,3])) # 3
print(solution([1,2,4,5])) # 0
print(solution([1,1,1,1,1,1,2])) # 4