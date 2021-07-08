#1 n입력받기
n=int(input())
arr=list(map(int,input().split()))
dp=[0]*n
dp[0]=arr[0]
'''
for i in range(2,n+1):
    for j in range(i+1,n+1):
        if dp[i-1]+arr[i-1]>dp[i-1]:
            dp[i]=dp[i-1]+arr[i-1]
        else:
            dp[i]=dp[i-1]
            break
'''

#dp이전값에 현재 i번째의 배열수를 더한것(이전까지의 모든수의 합)이 i번째 배열수보다 크면 그값으로 바꾼다.
for i in range(1,n):
    dp[i]= max(dp[i-1]+arr[i],arr[i])
print(max(dp))