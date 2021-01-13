def solution(triangle):
    while True:
        bottom = triangle.pop(-1)
        if len(bottom) == 1:
            return bottom[0]
        for i in range(len(bottom)-1):
            if bottom[i] > bottom[i+1]:
                triangle[-1][i] += bottom[i]
            else:
                triangle[-1][i] += bottom[i+1]

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))