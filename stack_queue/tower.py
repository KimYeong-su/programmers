# 탑(https://programmers.co.kr/learn/courses/30/parts/12081)
# 입출력 예
# heights	        return
# [6,9,5,7,4]	    [0,0,2,2,4]
# [3,9,9,3,5,7,2]	[0,0,0,3,3,3,6]
# [1,5,3,6,7,6,5]	[0,0,2,0,0,5,6]


def solution(heights):
    answer = []
    for i in range(len(heights)):
        temp = []
        for j in range(i):
            if heights[i] < heights[j]:
                temp.append(j+1)
        if len(temp)!=0:
            answer.append(max(temp))
        else:
            answer.append(0)
    return answer