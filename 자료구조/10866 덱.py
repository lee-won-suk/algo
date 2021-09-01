import sys
from collections import deque
input=sys.stdin.readline
#N입력
n=int(input())
dec=deque()
for i in range(n):

    order=list(input().split())
    if order[0]=='push_front':
        dec.appendleft(order[1])
    elif order[0]=='push_back':
        dec.append(order[1])
    elif order[0] == 'pop_front':
        if dec:
            data=dec.popleft()
            print(data)
        else:
            print(-1)
    elif order[0] == 'pop_back':
        if dec:
            data=dec.pop()
            print(data)
        else:
            print(-1)
    elif order[0] == 'size':
        print(len(dec))
    elif order[0] == 'empty':
        if not dec:
            print(1)
        else:
            print(0)
    elif order[0] == 'front':
        if not dec:
            print(-1)
        else:
            print(dec[0])
    elif order[0] == 'back':
        if not dec:
            print(-1)
        else:
            print(dec[-1])