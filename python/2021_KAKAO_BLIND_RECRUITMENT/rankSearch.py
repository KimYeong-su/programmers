from itertools import combinations
import copy
def case(l, score, idx, visit):
    global informations
    for i in range(4):
        if visit[i]: continue
        tmp = l[i]
        l[i] = '-'
        visit[i] = True
        if ' '.join(map(str,l)) in informations:
            informations[' '.join(map(str,l))] += [(score, idx)]
        else:
            informations[' '.join(map(str,l))] = [(score, idx)]
        case(l, score, idx, visit)
        l[i] = tmp
        visit[i] = False
    return

def solution(info, query):
    global informations
    answer = []
    informations = {}
    for idx, i in enumerate(info):
        tmp = list(map(str,i.split(' ')))
        score = int(tmp.pop())
        if ' '.join(map(str,tmp)) in informations:
            informations[' '.join(map(str,tmp))] += [(score, idx)]
        else:
            informations[' '.join(map(str,tmp))] = [(score, idx)]
        case(tmp, score, idx, [False for _ in range(4)])
    for q in query:
        tmp = list(map(str,q.split(' and ')))
        food, score = tmp.pop().split(' ')
        score = int(score)
        tmp.append(food)
        key = ' '.join(map(str, tmp))
        
        if key in informations.keys():
            tmp = list(sorted(set(informations[key])))
            left = 0
            right = len(tmp)-1
            result = float('inf')
            while left <= right:
                mid = (left + right) // 2
                
                if tmp[mid][0] < score:
                    left = mid+1
                else:
                    result = min(result,mid)
                    right = mid - 1
            if result == float('inf'):
                answer.append(0)
            else:
                answer.append(len(tmp) - result)
        else:
            answer.append(0)
    
    return answer


'''
def solution(info, query):
    global informations
    answer = []
    informations = {}
    for idx, i in enumerate(info):
        tmp = list(map(str,i.split(' ')))
        score = int(tmp.pop())
        for n in range(5):
            for case in combinations([0,1,2,3], n):
                tmp1 = tmp.copy()
                for c in case:
                    tmp1[c] = '-'
                if ' '.join(map(str,tmp1)) in informations:
                    informations[' '.join(map(str,tmp1))] += [(score, idx)]
                else:
                    informations[' '.join(map(str,tmp1))] = [(score, idx)]

    for q in query:
        tmp = list(map(str,q.split(' and ')))
        food, score = tmp.pop().split(' ')
        score = int(score)
        tmp.append(food)
        key = ' '.join(map(str, tmp))
        
        if key in informations.keys():
            tmp = list(sorted(set(informations[key])))
            left = 0
            right = len(tmp)-1
            result = float('inf')
            while left <= right:
                mid = (left + right) // 2
                
                if tmp[mid][0] < score:
                    left = mid+1
                else:
                    result = min(result,mid)
                    right = mid - 1
            if result == float('inf'):
                answer.append(0)
            else:
                answer.append(len(tmp) - result)
        else:
            answer.append(0)
    
    return answer
'''