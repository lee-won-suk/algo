#조합을 이용한 문제.
import math # 팩토리얼 사용을 위해서
#1 dp 테이블 초기화
#제한이 둘다 30미만이므로 30 30 으로 초기화
dp=[  [1]*30 for _ in range(30)  ]

#테이블 값 넣기
for j in range(1,30):
    for k in range(1,30):
        if j>=k:
            dp[j][k] =  int(    math.factorial(j) / (math.factorial(k) * math.factorial(j-k)) )
#테스트 케이스 입력
T=int(input())

for i in range(T):
    #사이트 개수 입력 받기
    N,M=map(int,input().split())
    print(dp[M][N])
