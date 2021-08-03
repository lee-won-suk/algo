import sys

input=sys.stdin.readline
#R,C입력
R,C=map(int,input().split())
#문자열 배열
Moke=[]
for _ in range(R):
    Moke.append(list(map(str,input())))
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    for i in range(R):
        for j in range(C):
            if Moke[i][j]=='W':
                for a in range(4):
                    nx=i+dx[a] #행
                    ny=j+dy[a] #열
                    if 0<=nx<R and 0<=ny<C:
                        if Moke[nx][ny]=='.':
                            Moke[nx][ny]='D'
                        elif Moke[nx][ny]=='S':
                            return 0
    return 1
ans=bfs()
print(ans)
for i in range(R):
    print(''.join(Moke[i])  )




