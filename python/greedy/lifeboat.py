from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    people = deque(people)
    while people:
        mini = people[0]
        maxi = people.pop()
        answer += 1
        if mini + maxi <= limit:
            try:
                people.popleft()
            except:
                continue
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))