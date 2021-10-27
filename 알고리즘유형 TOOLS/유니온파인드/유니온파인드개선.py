def find_parent(parent,x):
    if parent[x] !=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b]=a
    else:
        parent[a]=b

#노드와 간선 개수 입력
v,e=map(int,input().split())

#부모테이블 생성
parent=[0]*(v+1)
for i in range(1,v+1):
    parent[i]=i

#유니온 연산
for _ in range(e):
    a,b=map(int,input().split())
    union_parent(parent,a,b)

#각원소가 속한 집합 출력
for i in range(1,v+1):
    print(find_parent(parent,i), end=' ')

print()

for i in range(1,v+1):
    print(parent[i],end=' ')
