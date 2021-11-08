def solution(n, computers):
    #방문배열
    arr=[False]*(n)
    cnt=0
    for i in computers:
        if arr.count(True)==n:
            break
        for j in range(n):
            if i.count(1) == 1:
                cnt += 1
                break
            if i[j]==1 and arr[j]==False:
                arr[j]=True
    return cnt




def solution(n,computers):
    answer=0
    #방문배열
    visited=[False for i in range(n)]

    for com in range(n):
        #현재 원소가 방문한적 없으면
        if visited[com]==False:
            DFS(n,computers,com,visited)
            answer+=1
    return answer




def DFS(n,computers,com,visited):
    #현재원소 방문 표시
    visited[com]=True
    #원소내의 모든 연결요소중 자기자신을 제외한 연결요소
    for connect in range(n):
        if connect!=com and computers[com][connect]==1:
            #방문을 안했으면 그 원소에서 한번더 DFS
            if visited[connect]==False:
                DFS(n,computers,connect,visited)



#BFS
def solution(n,computers):
    answer=0
    #방문배열
    visited=[False for i in range(n)]

    for com in range(n):
        if visited[com]==False:
            BFS(n,computers,com,visited)
            answer+=1
    return answer

def BFS(n,computers,com,visited):
    from collections import deque
    q=deque()
    q.append(com)
    while q:
        com=q.popleft()
        visited[com] = True
        for connect in range(n):
            if com!=connect and computers[com][connect]==1:
                if visited[connect]==False:
                    q.append(connect)

print(solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]]))






