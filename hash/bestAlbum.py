def solution(genres, plays):
    answer = []
    g_c = {}
    for i in range(len(genres)):
        if genres[i] in g_c:
            g_c[genres[i]][0] += plays[i]
            g_c[genres[i]][1] += [(plays[i],i)]
        else:
            g_c[genres[i]] = [plays[i], [(plays[i],i)]]
    genres = sorted(g_c.values(), key = lambda x : -x[0])
    for tmp in genres:
        tmp = sorted(tmp[1],key = lambda x : (-x[0], x[1]))
        answer.append(tmp[0][1])
        try:
            answer.append(tmp[1][1])
        except:
            pass
    return answer

print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print(solution(["pop", "pop", "pop", "rap", "rap"], [45, 50, 40, 60, 70]))