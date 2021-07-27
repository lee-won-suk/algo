from collections import deque
#n,m 입력받기
n,m,r=map(int, input().split())
arr=[list(map(str,input().split())) for _ in range(n)]

limit=min(n,m)//2
def move(r):
    global limit,arr
    q=deque()
    nx,ny=0,0
    width=m
    height=n# 높이
    #1.반시계로 받기
    for a in range(limit):
        nx,ny=a,a

        for i in range(height-1):
            q.append(arr[ny+i][nx])
        for i in range(width - 1):
            q.append(arr[height-1+ny][i+nx])

        for i in range(height - 1):
            q.append(arr[height-1-i+ny][width-1+nx])

        for i in range(width - 1):
            q.append(arr[ny][width-1-i+nx])

        q.rotate(r)
        for i in range(height - 1):
           arr[ny + i][nx]=q.popleft()
        for i in range(width - 1):
            arr[height - 1 + ny][i + nx]=q.popleft()

        for i in range(height - 1):
            arr[height - 1 - i + ny][width - 1 + nx]=q.popleft()

        for i in range(width - 1):
            arr[ny][width - 1 - i + nx]=q.popleft()
        width-=2
        height-=2

move(r)
for i in range(n):
    print( ' '.join(arr[i]))