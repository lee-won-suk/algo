
N, M = map(int, input().split())  # M = depth
result = []
visitied = [False]*(N+1)

def dfs(depth, N, M):
    if depth == M+1:  # 깊이까지 탐색 완료
        for i in range(0,len(result)):
            print(result[i],end=" ")
        print()
        return
    for num in range(1,N+1):
        if not visitied[num]:
            visitied[num] = True
            result.append(num)
            dfs(depth+1, N, M)
            visitied[num] = False
            result.pop()

dfs(1,N,M)