s = ["aabbaccc","ababcdcdababcdcd","abcabcdede","abcabcabcabcdededededede","xababcdcdababcdcd"]
results = [7,9,8,14,17]

def solution(s):
    answer = float('inf')
    N = len(s)
    if N == 1:
        return 1
    for i in range(1,N//2+1):
        case = []
        for j in range(0,N,i):
            case.append(s[j:j+i])
        cnt = 0
        now = case[0]
        tmp = ''
        for c in range(1,len(case)):
            prev = case[c]
            if now == prev:
                cnt += 1
                continue
            else:
                if cnt:
                    tmp += str(cnt+1) + now
                else:
                    tmp += now
                now = prev
                cnt = 0
        else:
            if cnt:
                tmp += str(cnt+1) + now
            else:
                tmp += prev
        if answer > len(tmp):
            answer = len(tmp)
            
    return answer

for i in range(len(results)):
    if results[i] != solution(s[i]):
        print('Fail')
        break
else:
    print('Collect')