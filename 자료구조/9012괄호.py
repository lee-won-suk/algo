from collections import deque
#T입력
T=int(input())
flag=False
for i in range(T):
    Str=list(input())
    queue=deque()
    for ps in Str:
        if ps=='(':
            queue.append(ps)
        else:
            if not queue:
                print('NO')
                flag=True
                break
            queue.pop()
    if not queue and flag==False:
        print('YES')
    if queue:
        print('NO')
    flag=False
