# 전화번호 목록(https://programmers.co.kr/learn/challenges?selected_part_id=12077)
# phone_book	                return
# [119, 97674223, 1195524421]	false
# [123,456,789]	            true
# [12,123,1235,567,88]	    false

def solution(phone_book):
    answer = True
    phone_book = list(sorted(phone_book))
    for i in range(len(phone_book)):
        for j in range(i+1,len(phone_book)):
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                answer = False
                break
        if answer == False:
            break
    return answer


'''
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):   # str.startwith('ppp')는 ppp로 str이 시작하는 확인해주는 함수
            return False
    return True
'''