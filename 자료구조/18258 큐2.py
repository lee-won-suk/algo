from collections import deque
import sys
input=sys.stdin.readline
#N입력
N=int(input())

queue=deque()

for i in range(N):
    order=list(map(str,input().split()))
    if order[0]=='push':
        queue.append(order[1])
    elif order[0] == 'pop':
        if not queue:
            print(-1)
            continue
        data=queue.popleft()
        print(data)
    elif order[0] == 'size':
        print(len(queue))
    elif order[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)