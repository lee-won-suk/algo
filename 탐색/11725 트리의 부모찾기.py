import sys
input=sys.stdin.readline
#N 입력
N=int(input())
#그래프 입력
graph=[ [] for _ in range(N+1) ]

for i in range(N-1):
    n1,n2 =map(int,input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

queue=[1]
visit=[0]*(N+1)
result={}

while queue:
    node=queue.pop()
    for i in graph[node]:
        if visit[i]==0:
            result[i]=node
            visit[i]=1
            queue.append(i)
'''
def dfs(start):
    need_visit=[start]
    visited=[]

    while need_visit:
        node = need_visit.pop(0)
        if node==1:
            return True
        if node not in visited:
            for i in graph[node]:
                need_visit.append(i)
            visited.append(node)
    return False
def FindRoot(node):
    stack=[]
    if len(graph[node])==1:
        return graph[node].pop()

    else:
        for i in graph[node]:
            stack.append(i)

        if 1 in stack:
            return 1

        else:
            left=stack.pop()
            right=stack.pop()
            if dfs(left)==True:
                return left
            else:
                return right
'''

for i in range(2, N+1):
    print(result[i])



