#n입력
n=int(input())
arr=[ list(map(int, input().split()) ) for _ in range(n)]
#배열입력
dp=[  [0]*n for _ in range(n)  ]
dp[0][0]=1
for i in range(n):
    for j in range(n):
     if dp[i][j]!=0 and arr[i][j]!=0:
        if arr[i][j]+i<n :
         dp[i+arr[i][j] ][j]+=dp[i][j]
        if  arr[i][j]+j<n :
         dp[i][j+arr[i][j]]+= dp[i][j]
print(dp)
print(dp[n-1][n-1])
