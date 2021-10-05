

def solution(bridge_length, weight, truck_weights):
    time=0
    #다리 길이만큼 만들기
    bridge=[0]*bridge_length

    while len(bridge)!=0:
        time+=1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge)+truck_weights[0]<=weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return time

b,w,t=100,	100,	[10]
print(solution(b,w,t))