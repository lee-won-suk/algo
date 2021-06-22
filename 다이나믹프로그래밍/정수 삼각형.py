#삼각형 크기 입력받기
size=  int(input())
#정수삼각형 입력받기
dp=[]
for i in  range(size):
    dp.append( list(map( int,input().split()) )  )


#각각의 정수 삼각형 자리를 최대값으로 바꾼다
for i in range(1,size):
    for j in range(i+1):
     #1 대각선 왼쪽에서 왔을 경우
     if j==0:
         left=0
     else:
         left=dp[i-1][j-1]
     #2 대각선 오른쪽에서 왔을 경우
     if j==i:
         right=0
     else:
         right=dp[i-1][j]

     #최대값 갱신
     dp[i][j]=dp[i][j]+max(left,right)

print(  max( dp[size-1]) )
