#1 n 입력받기 바텀업
n=int(input())
#1 dp테이블 초기화
dp=[0]*(n+1)
#3.테이블 미리 생성.
dp[1]=1

for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[n])


'''
#1 n 입력 받기 탑다운
n=int(input())
#dp테이블
dp=[0]*(n+1)
dp[1]=1
dp[2]=2
def fibo(x):
    if x==0:
        return 0
    if x==1 or x==2:
        return 1
    elif dp[x]:
        return dp[x]
    else:
        dp[x]=fibo(x-1)+fibo(x-2)
        return dp[x]
print(fibo(n))
'''
