import sys
import heapq
INF=int(1e9)
input=sys.stdin.readline
n,m,k,start=map(int,input().split())

#각 노드별 거리 배열
graph=[ [] for _ in range(n+1) ]
distance= [INF]*(n+1)

# 간선 정보 입력받기
for i in range(m):
    a,b=map(int,input().split())
    graph[a].append( (b,1)  )


#다익스트라
def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))

    distance[start]=0

    while q: #큐가 안비어있을 때 까지
        #가장 최단 거리 짧은 노드 꺼내기
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue

        #현재노드와 인접한 다른노드들 확인
        for i in graph[now]:
            #최단거리 새로 구하기
            cost=dist+i[1]
            if cost < distance[i[0]]:
                #거리 갱신
                distance[i[0]]=cost
                heapq.heappush(q, (cost,i[0]) )

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==k:
        print(i)
if k not in distance:
    print(-1)