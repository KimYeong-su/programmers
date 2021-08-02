enroll = [["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]]
referral = [["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]]
seller = [["young", "john", "tod", "emily", "mary"], ["sam", "emily", "jaimie", "edward"]]
amount = [[12, 4, 2, 5, 10], [2, 3, 5, 4]]
result = [[360, 958, 108, 0, 450, 18, 180, 1080], [0, 110, 378, 180, 270, 450, 0, 0]]

def solution(enroll, referral, seller, amount):
    global money
    answer = []
    n = len(enroll)
    graph = {}
    money = {}
    for i in range(n):
        graph[enroll[i]] = referral[i]
        money[enroll[i]] = 0
    def calc(person, graph, cost):
        global money
        up = int(cost * 0.1)
        my = cost - up
        money[person] += my
        if graph[person] == '-' or up == 0: # 0원이면 return 해주지 않으면 recursionError 걸린다.
            return
        calc(graph[person], graph, up)
        
    for idx,sell in enumerate(seller):
        calc(sell, graph, amount[idx]*100)
    for en in enroll:
        answer.append(money[en])
    return answer

for i in range(len(enroll)):
    if solution(enroll[i], referral[i], seller[i], amount[i]) != result[i]:
        print('Fail')
        exit()
else:
    print('Collect!!')
