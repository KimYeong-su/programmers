def solution(N, number):
    if N == number:
        return 1
    check = [set() for x in range(8)]
    for idx, x in enumerate(check, start=1):
        x.add(int(str(N) * idx))
    for i in range(1,8):
        for j in range(i):
            for op1 in check[j]:
                for op2 in check[i-j-1]:
                    check[i].add(op1 + op2)
                    check[i].add(op1 - op2)
                    check[i].add(op1 * op2)
                    if op2:
                        check[i].add(op1 // op2)
        if number in check[i]:
            return i + 1
    return -1

print(solution(5, 12))
print(solution(2, 11))