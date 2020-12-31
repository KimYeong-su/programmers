def solution(begin, target, words):
    global answer
    if target not in words:
        return 0
    def check(begin, target, words, l, cnt):
        global answer
        if begin == target:
            if answer > cnt:
                answer = cnt
            return
        for word in words:
            if word in l: continue
            tmp = 0
            for i in range(len(word)):
                if word[i] != begin[i]:
                    tmp+=1
            if tmp==1:
                l.append(word)
                check(word, target, words, l, cnt+1)
                l.pop(-1)
    answer = 1000
    check(begin, target, words, [], 0)
    return answer

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))