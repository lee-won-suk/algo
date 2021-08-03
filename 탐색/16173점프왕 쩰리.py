import sys

input=sys.stdin.readline
#n입력
N=int(input())
#게임 배열 입력
arr=[ list(map(int,input().split())) for _ in range(N)]

dx=[1,0]
dy=[0,1]

def jump():
    need_visit=[[0,0]]
    visited=[[0]* N for _ in range(N)]

    while need_visit:
        x, y = need_visit.pop(0)

        if arr[x][y] == -1:
            return True
        jum=arr[x][y]

        for i in range(2):
            nx=x+dx[i]*jum
            ny = y + dy[i] * jum
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny]==0:
               visited[nx][ny]=1
               need_visit.append([nx,ny])
    return False





if jump()==True:
    print("HaruHaru")
else:
    print("Hing")