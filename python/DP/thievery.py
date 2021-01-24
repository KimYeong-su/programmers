# 첫번째를 포함하면 처음은 무조건 0인덱스를 시작값으로 갖고 1인덱스는 0이 선택 되었으므로 선택이 안되기 때문에 0인덱스를 갖게 된다. 2인덱스는 0이든 아니든 0인덱스와 더해지면 최대값을 갖는다.
# 마찬가지 방법으로 첫번째를 선택하지 않으면 처음은 0값을 넣어주면 되고 1인덱스는 무조건 선택 될 수 밖에 없으므로 시작 리스트에 넣어준다. 다음 2인덱스는 1인덱스를 선택했다면 고를 수 없고 아니라면 선택할 수 있으므로 1번과 2번의 max값 비교로 1번을 선택할지 안할지 비교한다.
# https://programmers.co.kr/questions/7619


def solution(money):
    if len(money) == 3:
        return max(money)
    start0 = [money[0], money[0], money[0]+money[2]] 
    start1 = [0, money[1], max(money[1],money[2])]
    for i in range(3, len(money)):
        start0.append(max(start0[i-2], start0[i-3]) + money[i])
        start1.append(max(start1[i-2], start1[i-3]) + money[i])
    return max(start0[-2], start0[-3], start1[-1], start1[-2])

print(solution([1,2,3,1]))
print(solution([1,1,4,1,4]))
print(solution([[1000, 0, 0, 1000, 0, 0, 1000, 0, 0, 1000]]))
print(solution([1000, 1, 0, 1, 2, 1000, 0]))
print(solution([1000, 0, 0, 0, 0, 1000, 0, 0, 0, 0, 0, 1000]))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(solution([0, 0, 0, 0, 100, 0, 0, 100, 0, 0, 1, 1]))
print(solution([11, 0, 2, 5, 100, 100, 85, 1]))
print(solution([1, 2, 3]))
