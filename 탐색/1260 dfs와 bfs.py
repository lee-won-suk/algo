import sys
input=sys.stdin.readline

# N,M,V입력
N,M,V=map(int,input().split())
arr=[[] for _ in range(N+1) ]
for _ in range(M):
    key,value=map(int,input().split())
    arr[key].append(value)
    arr[value].append(key)

for i in range(1,len(arr)):
    arr[i].sort()
def bfs(start):
    need_visit=[start]
    visited=[]
    while need_visit:
        node=need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            for i in arr[node]:
                 need_visit.append(i)
    return visited
def dfs(start):
    need_visit=[start]
    visited=[]
    while need_visit:
        node=need_visit.pop()
        if node not in visited:
            visited.append(node)

            for i in sorted(arr[node],reverse=True):
                 need_visit.append(i)
    return visited

bfsList=bfs(V)
dfsList=dfs(V)

print(' '.join( map(str,dfsList)) )
print(' '.join (map(str,bfsList)) )
