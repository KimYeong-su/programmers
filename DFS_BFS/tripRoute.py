def solution(tickets):
    global answer
    answer = []
    N = len(tickets)
    visit = [False] * N
    def check(tickets, visit, result):
        global answer
        if False not in visit:
            answer.append(result)
            return
        for i in range(N):
            if visit[i]: continue
            s,e = tickets[i]
            if s == result[-1]:
                visit[i] = True
                check(tickets, visit, result + [e])
                visit[i] = False
    
    check(tickets, visit, ['ICN'])
    answer.sort()
    return answer[0]

print(solution([['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]))
print(solution([['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]))