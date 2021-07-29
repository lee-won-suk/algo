from collections import deque
import sys
input=sys.stdin.readline

#N,L,R 입력받기
N,L,R=map(int,input().split())
#인구수 배열
A=[list(map(int,input().split())) for _ in range(N) ]

cnt=0
dy=[-1,0,1,0]
dx=[0,1,0,-1]

#인접한곳중 조건에 맞는 모든 지역을 temp에 담아 넣는데, 이를 bfs로 이용했다.
def UnionCheck(i,j):
    need_visit=deque() #방문해야할 지역 큐로
    need_visit.append([i,j])
    temp=[]
    temp.append([i,j])#총 연합 지역을 담을 큐이다.
    while need_visit:
        y,x=need_visit.pop()
        for i in range(4):
            ny=y+dy[i]
            nx= x + dx[i]
            if 0<=nx<N and 0<=ny<N and visit[ny][nx]==0: # 범위내에 들어가고, L과 R사이에 범위에 존재하면
                if L<=abs(A[ny][nx]-A[y][x])<=R:
                    visit[ny][nx]=1 # 연합을 맻은 곳은 1로 표시
                    need_visit.append([ny,nx])#큐에 넣어서 bfs 활용
                    temp.append([ny, nx])#방문한 지역 따로 저장
    return temp

while True:
    visit=[[0]*N for _ in range(N)] # 이미 연합인 지역 체크
    isUnion=False
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0: # 방문을 안한 지역이면 1로 만들고 연합이 이미 돼어있다는 표시.
                visit[i][j]=1
                temp=UnionCheck(i,j)
                if len(temp)>1: # 연합을 한지역이상 했으면
                    isUnion=True
                    num=sum(  [ A[y][x] for y,x in temp ]  )//len(temp) #인구수 분배
                    for y,x in temp:
                        A[y][x]=num
    if not isUnion: #연합이 없다는 얘기는 이동이 없었다는 얘기이므로로
       break
    cnt+=1
print(cnt)