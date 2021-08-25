import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)#무한 값 의미

# 노드의 개수, 간선의 개수, 시작노드 입력받기
n,m,c=map(int,input().split())

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph=[[] for _ in range(n+1)]

#최단거리 테이블 무한으로 초기화
distance=[INF]*(n+1)

#모든 간선 정보 입력받기.
for i in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z)) # x번 노드에서 y번 노드로 이동하는데 비용이 z라는 의미.  ( 다음노드, 비용)의 형태로 입력.


def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))#시작노드를 가기위한 거리는 0으로 설정. ( 거리, 다음노드) 첫번째원소로 정렬되는 최소힙을 이용하려고 비용을 첫번쨰원소로 둠,
    distance[start]=0

    while q:#큐에 원소가 존재할 때까지
        #가장 거리가 짧은 노드에 대한 정보 꺼내기
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        #현재노드와 인접한 모든 노드들을 확인한다.
        for i in graph[now]:
            cost=dist+i[1] #cost=현재 노드거리 + 인접노드의 거리  graph 에는 (다음도시, 거리) 이렇게 삽입했음.
            #현재노드를 거쳐서 다른노드로 이동하는 거리가 더 짧은 경우에
            if cost<distance[i[0]]:
                distance[i[0]]=cost #갱신
                heapq.heappush(q,(cost,i[0])) #큐에 추가
dijkstra(c)
print(distance)
cnt=0 #도달 가능한 도시 개수
max_distance=0#도달가능한 노드중 가장 멀리있는 노드의 최단거리
for d in distance:
    if d!=INF and d!=0 :
        cnt+=1
        max_distance=max(max_distance, d)
print(cnt,max_distance,end=' ')
