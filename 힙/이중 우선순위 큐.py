def solution(operations):
    import heapq
    heap=[]#최소힙
    for i in operations:
        order,num=i.split()
        if order=="I":
            heapq.heappush(heap,int(num))

        elif order=="D" and len(heap)>0:
            if int(num)==1:
                #최대힙으로 변환후 삭제
                temp=list(heap)
                temp.sort()
                temp.pop()
                heap=temp
                heapq.heapify(heap)
            else:
                heapq.heappop(heap)

    if len(heap)>0:
        min=heapq.heappop(heap)
        temp = list(heap)
        temp.sort()
        max=temp.pop()
    else:
        min,max=0,0
    answer = [max,min]
    return answer

def solution(operations):
    import heapq
    heap=[]#최소힙
    for i in operations:
        order,num=i.split()
        if order=="I":
            heapq.heappush(heap,int(num))
        elif order=="D" and len(heap)>0:
            if int(num)==1:
                heap.remove(max(heap))
            else:
                heapq.heappop(heap)

    if not heap:
        return [0,0]
    return [max(heap),heap[0]]

#o=["I 7","I 5","I -5","D 1"]
o=["I 16","D 1"]
solution(o)

#최댓값 제거 -> heap.remove(max(heap))
# 원소 없을 경우 : if not heap