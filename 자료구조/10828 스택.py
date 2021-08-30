from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
arr=deque()

for i in range(n):
    order=list(map(str,input().split()))
    if order[0]=='push':
        arr.append(order[1])
    elif order[0] == 'pop':
        if not arr:
            print(-1)
        else:
            data=arr.pop()
            print(data)
    elif order[0] == 'size':
        print(len(arr))
    elif order[0] == 'empty':
        if not arr:
            print(1)
        else:
            print(0)
    elif order[0]=='top':
        if not arr:
            print(-1)
        else:
            print(arr[-1])
