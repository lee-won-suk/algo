#리벤슈타인 알고리즘을 사용해준다.
def edit_dist(str1,str2):
    n=len(str1)#문자열1의 길이
    m=len(str2)#문자열2의 길이

    #dp2차원 테이블 초기화  n의개수가 행, m의 개수가 열
    #m+1,n+1인 이유 : 0번째부터 n번째까지 넣기 위해서.
    dp= [ [0]*(m+1) for _ in range(n+1) ]

    #초기 설정
    for i in range(m+1):
        dp[0][i]=i
    for j in range(n+1):
        dp[j][0]=j


    #최소 편집거리 알고리즘 사용

    for i in range(1,n+1):
        for j in range(1,m+1):
            #두 문자가 같으면 왼쪽위의 편집거리와 일치
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]

            #두 문자가 다르면 왼쪽,왼쪽위,위 중 min+1
            else:
                dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
    return dp[n][m]
str1=input()
str2=input()
print(edit_dist(str1,str2))