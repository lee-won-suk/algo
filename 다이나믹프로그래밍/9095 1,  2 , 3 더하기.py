#테스트 케이스 T
T=int(input())
#dp[i] i번째 수일 때의 방법의 개수
dp=[0]*11
dp[1]=1
dp[2]=2
dp[3]=4
for i in range(T):
    n=int(input())
    for i in range(4,n+1):
        dp[i]=dp[i-1]+dp[i-2]+dp[i-3]

    print(dp[n])
