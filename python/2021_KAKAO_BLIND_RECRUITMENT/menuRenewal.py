from itertools import combinations
from collections import Counter

'''
# collections의 Counter 함수 배우고 갑니다.
# https://programmers.co.kr/learn/courses/30/lessons/72411

def solution(orders, course):
    result = []

    for course_size in course:
        order_combinations = []
        for order in orders:
            order_combinations += combinations(sorted(order), course_size)

        most_ordered = Counter(order_combinations).most_common()
        result += [ k for k, v in most_ordered if v > 1 and v == most_ordered[0][1] ]

    return [ ''.join(v) for v in sorted(result) ]
'''

def solution(orders, course):
    answer = []
    for c in course:
        menus = {}
        for order in orders:
            if c <= len(order):
                for i in combinations(order, c):
                    menu = ''.join(map(str,sorted(i)))
                    if menu in menus.keys():
                        menus[menu] += 1
                    else:
                        menus[menu] = 1
        answer += list(filter(lambda x: menus[x]>1 and menus[x] == max(menus.values()), menus.keys()))
    return sorted(answer)

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])) # ["AC", "ACDE", "BCFG", "CDE"]
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])) # ["ACD", "AD", "ADE", "CD", "XYZ"]
print(solution(["XYZ", "XWY", "WXA"], [2,3,4])) # ["WX", "XY"]