#기능개발(https://programmers.co.kr/learn/courses/30/parts/12081)
# progresses	speeds	    return
# [93,30,55]	[1,30,5]	[2,1]

def solution(progresses, speeds):
    answer = []
    time = []
    for i in range(len(progresses)):
        if (100-progresses[i])%speeds[i]:
            time += [(100-progresses[i])//speeds[i]+1]
        else:
            time += [(100-progresses[i])//speeds[i]]
    temp = 0
    for i in range(1,len(time)):
        if time[temp]<time[i]:
            answer += [i-temp]
            temp = i
        if i==len(time)-1:
            answer += [i-temp+1]
    return answer