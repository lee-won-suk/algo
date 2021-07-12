from sys import maxsize
#도시개수n 과 인원수c 입력
c,n=map(int, input().split())
arr=[list(map(int,input().split() )) for _ in range(n) ]
#dp[i]= i 인원일때 최소비용
dp=[0]+ [maxsize]*(c+100)

for cost,customer in arr:
    for i in range(customer,c+101):
        dp[i]=min(dp[i],dp[i-customer]+cost  )
print(min(dp[c : c+101]  ))