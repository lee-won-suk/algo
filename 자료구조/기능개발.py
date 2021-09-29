# def solution(progresses, speeds):
#     from collections import deque
#     day=deque()
#     for i in range(len(progresses)):
#         day.append( (100-progresses[i])//speeds[i] )
#     #현재값보다 클때까지 pop해서 개수세기
#     cnt=0
#     now=day[0]
#     answer = []
#     for i in day:
#         if now>=i:
#             cnt+=1
#         else:
#             now=i
#             answer.append(cnt)
#             cnt=1
#     answer.append(cnt)
#     '''while day:
#         idx=day.popleft()
#         if now>=idx:
#             cnt+=1
#         else:
#             now=idx
#             answer.append(cnt)
#             cnt=1
#     answer.append(cnt)
#     '''
#     return answer

def solution(progresses, speeds):
    import math
    cnt = 0
    answer = []
    now = math.ceil ( (100 - progresses[0]) / speeds[0] )
    for i in range(len(progresses)):
        idx=math.ceil ( (100 - progresses[i])/speeds[i]  )
        if now >=idx :
            cnt+=1
        else:
            now=idx
            answer.append(cnt)
            cnt=1
    answer.append(cnt)
    return answer


p=[96,94]
s=[3,3]
print(solution(p,s))