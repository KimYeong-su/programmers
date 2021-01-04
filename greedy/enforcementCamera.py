def solution(routes):
    answer = 1
    N = len(routes)
    routes.sort()
    idx = 1
    tmp = [routes[0][0], routes[0][1]]
    while idx < N:
        s, e = routes[idx]
        if tmp[0] > s or s > tmp[1]:
            tmp = [s,e]
            answer += 1
        else:
            if tmp[1] > e:
                tmp = [s,e]
            else:
                tmp[0] = s
        idx += 1
    return answer

'''
# Best coding
def solution(routes):
    routes = sorted(routes, key=lambda x: x[1])
    last_camera = -30000

    answer = 0

    for route in routes:
        if last_camera < route[0]:
            answer += 1
            last_camera = route[1]

    return answer
'''

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))