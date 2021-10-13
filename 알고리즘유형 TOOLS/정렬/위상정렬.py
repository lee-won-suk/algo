from collections import deque
#노드의 개수와 간선 개수 입력받기
v,e=map(int, input().split())
#모든 노드에 대한 진입차수 0으로 초기화
indegree=[0]*(v+1)
#각 노드에 연결된 간선정보를 담기위한 연결리스트 초기화
graph=[[] for i in range(v+1) ]

#방향 그래프의 모든 간선 정보 입력받기
for i in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)# a에서 b로 이동가능
    indegree[b]+=1# 진입차수 1 증가

#위상정렬 함수
def topology_sort():
    result=[]
    q=deque()
    #처음시작시 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    #큐가 빌 때까지 반복
    while q:
        now=q.popleft()
        result.append(now)
        #원소랑 연결된 간선 지우기
        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)
    for i in result:
        print(i, end=' ')
topology_sort()

