import re
'''
# 정규 표현식을 공부할 수 있는 좋은 경험 이였습니다.
# https://programmers.co.kr/learn/courses/30/lessons/72410
def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub("[^0-9a-z_.-]", '', new_id)
    new_id = re.sub('[.]+','.',new_id)
    new_id = re.sub('^[.]|[.]$','',new_id)
    new_id = "a" if len(new_id)==0 else new_id[:15]
    new_id = re.sub('^[.]|[.]$','',new_id)
    return new_id if len(new_id)>2 else new_id + ''.join(map(str,[new_id[-1] for _ in range(0,3-len(new_id))]))
'''

def solution(new_id):
    new_id = new_id.lower()
    new_id = re.sub("[^0-9a-z_.-]", '', new_id)
    new_id = re.sub('[.]+','.',new_id)
    while len(new_id) > 0:
        if new_id[0] == '.':
            new_id = new_id[1:]
        else:
            break
    while len(new_id) > 0:
        if new_id[len(new_id)-1] == '.':
            new_id = new_id[:len(new_id)-1]
        else:
            break
    if len(new_id) == 0:
        new_id = 'a'
    elif len(new_id) > 15:
        new_id = new_id[:15]
        while True:
            if new_id[len(new_id)-1] == '.':
                new_id = new_id[:len(new_id)-1]
            else:
                break
    while len(new_id) < 3:
        new_id += new_id[-1]
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm")) # "bat.y.abcdefghi"
print(solution("z-+.^.")) # "z--"
print(solution("=.=")) # "aaa"
print(solution("123_.def")) # "123_.def"
print(solution("abcdefghijklmn.p")) # "abcdefghijklmn"