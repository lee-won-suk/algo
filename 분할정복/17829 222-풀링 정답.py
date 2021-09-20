import sys
input=sys.stdin.readline
def Find(x,y,temp):
    return sorted ([temp[x][y],temp[x][y+1],temp[x+1][y],temp[x+1][y+1]])[2]
def search(arr,n):
    #1개 남으면 정답 출력
    if n==1:
        return arr[0][0]
    #풀링한번 돌고 난 값들 저장할 배열
    new_arr=[ [] for _ in range(n//2)]
    for i in range(0,n,2): # 행의 각 시작점들
        for j in range(0,n,2): # 열의 각 시작점
            new_arr[i//2].append(Find(i,j,arr))
    return search(new_arr,n//2)
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
print(search(arr,N))