#수열 크기
n=int(input())
#수열
arr=list(map(int,input().split()))
dp=[0]*n
dp=arr[:]
for i in range(1,n):
    for j in range(i):
        if arr[i]>arr[j]:
            dp[i]=max(dp[j]+arr[i],dp[i])
print(max(dp))