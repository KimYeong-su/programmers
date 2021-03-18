'''
# https://dev-note-97.tistory.com/156
# 시간을 초로 바꾸기!!
# memoization 하는 방법을 알 수 있었다.
# 시작 지점, 끝 지점을 +1 -1 을 통해 한번 누적 계산은 1초간의 누적 수
# 두번의 누적 계산은 전체의 누적 수를 갖게 된다는 점이 가장 키포인트였다.
# 원리를 이해 하면 생각보다 간단한 문제 였습니다.
'''

def change_sec(time):
    h,m,s = map(int, time.split(':'))
    return (60*60*h) + (60*m) + s

def change_str(sec):
    tmp = []
    if sec//3600 < 10:
        tmp.append('0'+str(sec//3600))
    else:
        tmp.append(sec//3600)
    m = sec%3600
    if m//60 < 10:
        tmp.append('0'+str(m//60))
    else:
        tmp.append(m//60)
    if m%60 < 10:
        tmp.append('0'+str(m%60))
    else:
        tmp.append(m%60)
    return ':'.join(map(str,tmp))

def solution(play_time, adv_time, logs):
    play_time_sec = change_sec(play_time)
    adv_time_sec = change_sec(adv_time)
    start_sec = []
    end_sec = []
    for log in logs:
        start, end = log.split('-')
        start_sec.append(change_sec(start))
        end_sec.append(change_sec(end))
    total_time = [0]*(play_time_sec+1)
    for i in range(len(logs)):
        total_time[start_sec[i]] += 1
        total_time[end_sec[i]] -= 1
    for _ in range(2):
        for i in range(1,play_time_sec+1):
            total_time[i] += total_time[i-1]
    maximum = 0
    answer_sec = 0
    for i in range(adv_time_sec-1,play_time_sec):
        if i >= adv_time_sec:
            if maximum < total_time[i] - total_time[i-adv_time_sec]:
                maximum = total_time[i] - total_time[i-adv_time_sec]
                answer_sec = i - adv_time_sec + 1
        else:
            if maximum < total_time[i]:
                maximum = total_time[i]
                answer_sec = i - adv_time_sec+1
    return change_str(answer_sec)

print(solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])) # "01:30:59"
print(solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])) # "01:00:00"
print(solution("50:00:00", "50:00:00", ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"])) # "00:00:00"