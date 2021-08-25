import sys
input=sys.stdin.readline
n,m=map(int,input().split())
INF=1e9#추가
graph=[ [INF] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    graph[i][i]=0

for _ in range(m):
    s,e=map(int,input().split())
    graph[s][e]=1
    graph[e][s] = 1 #양방향이라서 추가해줘야댐. 그래프같은 느낌
x,k=map(int,input().split())
print(x,k)
for k in range(1,n+1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

distance=graph[1][k]+graph[k][x]
if distance==INF:
    print(-1)
else:
    print(distance)