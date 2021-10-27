def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

#노드, 간선개수입력 받기.
v,e=map(int,input().split())
parent=[0]*(v+1)

#모든 간선 리스트, 최종비용을 담을 변수
edges=[]
result=0

#부모테이블 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i


for i in range(e):
    a,b,cost=map(int,input().split())
    #비용순으로 정렬하기 위해 튜플의 첫번째 원소를 비용으로 지정
    edges.append((cost,a,b))

#간선을 비용순으로 정렬
edges.sort()


#간선 하나씩 확인
for cost,a,b in edges:
    #사이클을 확인해서 안생기면union 생기면
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        #비용 더하기
        result+=cost

print(result)

