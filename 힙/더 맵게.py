def solution(scoville, K):
    import heapq
    '''b=[]
    for i in scoville:
        heapq.heappush(b, i)
    '''
    heapq.heapify(scoville)
    answer = 0
    while scoville[0]<K:
        if len(scoville)==1:
            return -1
        idx1=heapq.heappop(scoville)
        idx2=heapq.heappop(scoville)
        heapq.heappush(scoville,idx1+idx2*2)
        answer+=1
    return answer


a=[1, 2, 3, 9, 10, 12]
print( solution(a,7))
