# 위장(https://programmers.co.kr/learn/courses/30/parts/12077)
# clothes	                                                                        return
# [[yellow_hat, headgear], [blue_sunglasses, eyewear], [green_turban, headgear]]	5
# [[crow_mask, face], [blue_sunglasses, face], [smoky_makeup, face]]	            3

def solution(clothes):
    answer = 1
    dic = {}
    for i in clothes:
        if i[1] not in dic:
            dic[i[1]] = 2
        else:
            dic[i[1]] += 1
    cnt = list(dic.values())
    if len(cnt)==1:
        return cnt[0]-1
    for i in cnt:
        answer *= i
    answer -= 1
    return answer