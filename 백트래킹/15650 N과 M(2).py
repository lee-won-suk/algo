N,M=map(int,input().split())
result=[]#정답 출력용
visited=[False]*(N+1)#가지치기용. 갈필요없는 길을 막아준다.

def dfs(N,M,depth): #depth= M개까지 출력했는지 확인하려고.
    if depth==M+1:
        for i in result:
            print(i,end=" ")
        print()
        return

    for i in range(1,N+1):
        if not visited[i] :
            if len(result)!=0 and result[-1]>i:
                continue

            visited[i] =True
            result.append(i)
            dfs(N,M,depth+1)
            visited[i]=False
            result.pop()

dfs(N,M,1)