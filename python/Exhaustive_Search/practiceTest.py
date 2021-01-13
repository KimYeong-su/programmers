def solution(answers):
    answer = []
    a = [x for x in range(1,6)] * 2000
    b = [2,1,2,3,2,4,2,5] * 1250
    c = [3,3,1,1,2,2,4,4,5,5] * 1000
    aa = 0
    ab = 0
    ac = 0
    for an in range(len(answers)):
        tmp = answers[an]
        if a[an] == tmp:
            aa += 1
        if b[an] == tmp:
            ab += 1
        if c[an] == tmp:
            ac += 1
    flag = max(aa,ab,ac)
    if aa == flag:
        answer.append(1)
    if ab == flag:
        answer.append(2)
    if ac == flag:
        answer.append(3)
    return answer

print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))