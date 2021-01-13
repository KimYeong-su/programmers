def solution(number, k):
    stack = []
    for i in range(len(number)):
        if not stack:
            stack.append(number[i])
            continue
        flag = False
        while stack and int(stack[-1]) < int(number[i]):
            k -= 1
            stack.pop(-1)
            
            if not k:
                flag = True
                break
            
        
        stack.append(number[i])
        if flag:
            return ''.join(map(str, stack)) + number[i+1:]
    return ''.join(map(str, stack[:i+1-k]))

print(solution("1924", 2))
print(solution("1231234", 3))
print(solution("4177252841", 4))