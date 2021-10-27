def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)
    if a<b:
        parent[b]=a
    else: parent[a]=b
def solution(n, costs):
    total_cost=0
    #노드=n개  간선=len(costs)

    parent=[i for i in range(n+1)]
    costs.sort(key=lambda x:x[2])

    for v1,v2,cost in costs:
        if find_parent(parent,v1)!=find_parent(parent,v2):
            union_parent(parent,v1,v2)
            total_cost+=cost

    return total_cost


print( solution(4 ,[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]) )