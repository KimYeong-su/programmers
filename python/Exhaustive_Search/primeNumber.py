from itertools import permutations
def solution(numbers):
    numbers = list(numbers)
    check = set()
    for i in range(1, len(numbers)+1):
        base = list(permutations(numbers, i))
        for j in base:
            tmp = ''.join(map(str, j))
            if int(tmp) == 2:
                check.add(int(tmp))
                continue
            elif int(tmp) in [0,1]: continue
            l = int(int(tmp) ** 0.5)
            for k in range(2,l+1):
                if not int(tmp)%k:
                    break
            else:
                check.add(int(tmp))
    answer = len(check)
    return answer

print(solution('17'))
print(solution('011'))