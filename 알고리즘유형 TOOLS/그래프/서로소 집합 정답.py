# 특정 원소가 속한 집합을 찾기 -> x의 루트노드를 반환한다.
def find_parent(parent, x):
    #루트 노드를 찾을때까지 따라들어가며 재귀호출 (루트노드는 자기자신이 부모노드이므로)
    if parent[x] != x: #루트노드가 아니면
        return find_parent(parent, parent[x]) #재귀호출
    return x #루트노드일때 자기자신을 반환

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
	#각각의 루트노드를 찾는다.
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b: #두 노드중 큰 노드의 부모를 바꿔준다.
        parent[b] = a
    else:
        parent[a] = b

#노드와 간선의 개수 입력
v,e = map(int, input().split())
parent = [0] * (v+1) #부모테이블

#초기상태 - 부모를 자기자신으로 초기화
for i in range(1,v+1):
    parent[i] = i

#Union연산 각각 수행
for i in range(e):
    a,b = map(int, input().split())
    union_parent(parent, a, b)

#각 원소가 속한 집합 출력
for i in range(1, v+1):
    print(find_parent(parent, i))

#부모테이블 내용 출력
for i in range(1, v+1):
    print(parent[i])