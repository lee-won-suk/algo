def solution(jobs):
    import heapq
    start,now,i=0,0,0 # 이전작업의 시작시간,현재 시간, 지금까지 작업한 개수
    start=-1# 0부터 시작하기 위해
    heap=[]
    answer = 0
    while i<len(jobs): #모든 작업이 끝날 때까지
        # 현재 시점에서 작업이 가능한게 있는지 찾기
        for j in jobs:
            if start<j[0]<=now:
                heapq.heappush(heap,[j[1],j[0]])#작업의 소요시간, 요청 시점으로 바꿔서 넣음. 소요시간 기준으로
                #최소힙을 만들어야 되서
        if len(heap)>0:
            current=heapq.heappop(heap)
            start=now#현재 시점에서부터 작업을 시작하려고
            now+=current[0]
            answer+=now-current[1]
            i+=1
        else:
            now+=1
    return int(answer/len(jobs))