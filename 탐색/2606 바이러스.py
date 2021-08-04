#컴퓨터 수 :C
C=int(input())
#연결된 쌍
N=int(input())
com=[ [] for _ in range(C+1) ]


for i in range(N):
    key,value=map(int,input().split())
    com[key].append(value)
    com[value].append(key)

def bfs(start):
    need_visit=[start]
    visited=[]

    while need_visit:
        node=need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            for i in com[node]:
                need_visit.append(i)

    return visited
arr=bfs(1)
print(len(arr)-1)
