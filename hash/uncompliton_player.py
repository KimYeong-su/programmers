#완주하지 못한 선수(https://programmers.co.kr/learn/challenges?selected_part_id=12077)
# participant	                            completion	                        return
# [leo, kiki, eden]	                        [eden, kiki]	                    leo
# [marina, josipa, nikola, vinko, filipa]	[josipa, filipa, marina, nikola]	vinko
# [mislav, stanko, mislav, ana]	            [stanko, ana, mislav]	            mislav

def solution(participant, completion):
    answer = ''
    dic = {}
    for i in participant:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i]+=1
    for i in completion:
        dic[i]-=1
        if dic[i]==0:
            del dic[i]
    answer = list(dic.keys())[0]
    return answer

'''
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

'''
'''
def solution(participant, completion):
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    return answer
'''