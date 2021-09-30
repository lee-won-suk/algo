def solution(priorities, location):
    from collections import deque
    tmp=sorted(priorities,reverse=True)
    cnt=0#현재 가장큰수 인덱스
    # 순위기록
    answer=0
    locate=[0]*len(priorities)
    locate[location]=1
    #중요도 문자열
    temp=deque(zip(priorities,locate))
    while True:
        P,find=temp[0][0],temp[0][1]
        if P==tmp[cnt]:
            answer += 1
            if find==1:
                return answer
            cnt+=1
            temp.popleft()
        else:
            temp.rotate(-1)
p,l=[1, 1, 9, 1, 1, 1],0
print(solution(p,l))