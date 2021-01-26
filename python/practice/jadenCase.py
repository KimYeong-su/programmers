def solution(s):
    answer = ''
    flag = False
    for i in s:
        if i==' ':
            answer += i
            flag = False
        else:
            if flag:
                answer += i.lower()
            else:
                answer += i.upper()
                flag = True
                
    return answer

print(solution("3people unFollowed me")) # "3people Unfollowed Me"
print(solution("for the last week")) # "For The Last Week"
print(solution(" hEllo    1woRld  ")) # " Hello    1world  "
