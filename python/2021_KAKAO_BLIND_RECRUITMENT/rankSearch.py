'''
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
# https://velog.io/@study-dev347/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%EC%88%9C%EC%9C%84-%EA%B2%80%EC%83%89
# https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/
# 직접 구현한 코드는 효율성 통과가 되지 않네요.. 좀더 코드를 뜯어 봐야겠습니다.
import bisect

changes = []
tmp = []

def make_cases():
    global changes, tmp
    if len(tmp) == 4:
        t = []
        for index in tmp: t.append(index)
        changes.append(t)
        return
    for i in (False, True):
        tmp.append(i)
        make_cases()
        tmp.pop()

def replace(change, data):
    for i in range(4):
        if change[i]: data[i] = '-'
    return data

def copy(data):
    _data = []
    for item in data:
        _data.append(item)
    return _data

def search(scores, num):
    size = len(scores)
    return size - bisect.bisect_left(scores, num, lo=0, hi=size)

def solution(info, query):
    global changes
    answer = []
    info_dict = {}
    make_cases()

    for data in info:
        data = data.split(' ')
        score = int(data[-1])
        data = data[:4]

        for change in changes:
            _data = copy(data)
            _data = replace(change, _data)
            _data = ''.join(_data)

            if _data not in info_dict.keys(): info_dict[_data] = [score]
            else: info_dict[_data] += [score]

    for key in info_dict.keys(): info_dict[key].sort()

    for q in query:
        q = q.split(' ')
        score = int(q[-1])
        _q = ''

        for item in q[:len(q)-1]:
            if item != 'and': _q += item

        if _q not in info_dict.keys(): answer.append(0)
        else:
            cnt = search(info_dict[_q], score)
            answer.append(cnt)

    return answer