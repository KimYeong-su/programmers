def solution(brown, yellow):
    answer = []
    x = ((2+brown/2)+ ((2+brown/2)**2 - 4*(brown + yellow))**0.5)/2
    y = ((2+brown/2)- ((2+brown/2)**2 - 4*(brown + yellow))**0.5)/2
    if x > y:
        answer += [x,y]
    else:
        answer += [y,x]
    return answer

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))