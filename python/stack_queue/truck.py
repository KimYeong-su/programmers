# 다리를 지나는 트럭(https://programmers.co.kr/learn/courses/30/parts/12081)
# 입출력 예시
# bridge_length	weight	truck_weights	                return
# 2	            10	    [7,4,5,6]	                    8
# 100	        100	    [10]	                        101
# 100	        100	    [10,10,10,10,10,10,10,10,10,10]	110

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge=[]
    time=[]
    while len(truck_weights)!=0:
        if len(time)!=0 and answer-time[0]==bridge_length:
            bridge.pop(0)
            time.pop(0)
        if truck_weights[0]+sum(bridge)<=weight and len(bridge)<=bridge_length:
            bridge += [truck_weights.pop(0)]
            time += [answer]
        # print(bridge,time)
        answer += 1
    answer = time[-1]+bridge_length+1
    return answer