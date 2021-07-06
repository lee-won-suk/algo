#N입력받기
N=int(input())
#dp테이블 초기화
dp=[0]*(N+1)
dp[2]=1
for i in range(3,N+1):
    dp[i]=dp[i-1]+1
    if i % 3 == 0:
        dp[i] = min(dp[i//3]+1, dp[i])
    if i % 2 == 0:
        dp[i] =min(dp[i//2]+1, dp[i])
print(dp[N])