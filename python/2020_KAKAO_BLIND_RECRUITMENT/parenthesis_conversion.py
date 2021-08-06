p = ["(()())()", ")(", "()))((()"]
results = ["(()())()", "()", "()(())()"]

def solution(p):
    if not p:
        return ''
    u = ''
    v = ''
    for i in range(len(p)):
        u += p[i]
        if u.count('(') == u.count(')'):
            v = p[i+1:]
            break
    c = 0
    for i in range(len(u)):
        if u[i] == '(':
            c -= 1
        else:
            c += 1
        if c > 0:
            return '(' + solution(v) + ')' + ''.join(map(lambda x : ')' if x=='(' else '(', u[1:-1]))
        else:
            return (u + solution(v))

for i in range(len(results)):
    if results[i] != solution(p[i]):
        print('Fail')
        break
else:
    print('Collect')