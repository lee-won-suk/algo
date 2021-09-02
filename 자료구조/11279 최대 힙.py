import heapq
import sys
input=sys.stdin.readline
N=int(input())
queue=[]


for i in range(N):
    number=int(input())
    if number!=0:
        heapq.heappush(queue,-number)
    else:
        if not queue:
            print(0)
        else:
            data=heapq.heappop(queue)
            print(-data)

