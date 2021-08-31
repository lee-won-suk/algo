from collections import deque
import sys
#N입력
N=int(input())
arr=deque(i for i in range(1,N+1) )

for i in range(N):
    if len(arr)==1:
        print(arr[0])
        break
    else:
        arr.popleft()
        arr.rotate(-1)

