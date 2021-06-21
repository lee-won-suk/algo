
#테스트 케이스 입력
for tc in range(int(input()) ):
 #금광 정보 입력
 n,m=map(int,input().split())
 #초기 금광 정보
 array=list(map(int,input().split()   ))

 #2차원 dp테이블 초기화
 dp=[]
 index=0
 #인덱스 슬라이싱을 통해 index+m-1번째 까지의 원소까지 한행에 입력받아서 2차원 테이블을 만들어 낸다.
 for i in range(n):
    dp.append(array[index:index+m])
    index+=m

 #다이나믹 프로그래밍 실행
 #첫번째행인 0열은 시작지점이니 그대로 두고 1번째 열부터 m-1번째 열까지 진행하고
 #행은 0부터 시작해서 n-1열까지 진행한다.
 for j in range(1,m):
     for i in range(n):
      #1.왼쪽 위일 때
      #행이 0이면 왼쪽위가 없으므로 0
      if i==0:
          left_up = 0
      else:
          left_up=dp[i-1][j-1]
      # 2.왼쪽 아래일 때
      # 행이 n-1이면 왼쪽아래가 없으므로 0
      if i == n-1:
          left_down = 0
      else:
          left_down = dp[i+1][j-1]
      # 3.왼쪽에서 왔을 때
      left=dp[i][j-1]
      dp[i][j]=dp[i][j]+max(left_up,left,left_down)

 result=0
 #마지막 행의 열들 중 제일 큰 값이 최대값이 된다.
 for i in range(n):
    result=max(result, dp[i][m-1])
 print(result)