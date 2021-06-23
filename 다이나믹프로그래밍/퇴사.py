#일하는 날짜 N 입력받기
n=int(input())
#시간, 금액 나눠서 입력 받기
t=[]
p=[]
# dp테이블을 따로 주었다 . 뒤에서 부터 해결할 거기 때문에 초기화 필요
#dp[i] = i번째부터 끝까지 낼 수 있는 최대 이익
dp=[0]*(n+1)
max_value=0 #현재까지 최대 상담 금액

#값 분배해서 집어넣기
for _ in range(n):
    x,y=map(int, input().split())
    t.append(x)
    p.append(y)

#뒤에서 부터 확인
for i in range(n-1,-1,-1):
    time=t[i]+i #상담 기간 . 현재 날짜의 상담을 하면 걸리는 기간이다.
    #상담이 기간내에 끝나면
    if time <= n:# n-1이 아닌이유는 n이 7일때 7일차는 상담기간이 6과 같으니까.
        dp[i]=max(p[i]+dp[time],max_value)
        max_value=dp[i]
    #상담이 기간을 넘어가면
    else:
        dp[i]=max_value
print(max_value)