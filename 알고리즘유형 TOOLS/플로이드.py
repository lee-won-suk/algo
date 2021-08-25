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
    #양방향이면 추가 graph[e][s] = 1

for k in range(1,n+1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1, n + 1):
        if graph[i][j]==INF:
            print("inf")
        else:
            print(graph[i][j], end=' ')
    print