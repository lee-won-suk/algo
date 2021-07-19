#n입력 받기
n=int(input())
#출력할 배열
output=[ ['.'] * n for _ in range(n)         ]
#지뢰 위치 문자열 배열 입력받기
bomb=[]
open=[]
for i in range(n):
    bomb.append(list(input())    )
# 열린여부 배열 입력
for i in range(n):
    open.append(list(input())    )

#숫자 입력하기.
def insertNum(a,b):
    global n
    cnt=0
    arr=[-1,0,1]
    for i in arr:
       for j in arr:
           if 0<=a+i<n and 0<=b+j<n:
               if i==0 and j==0:
                   continue
               if bomb[a+i][b+j]=='*':
                   cnt+=1
    return cnt


def insertbomb():
    for i in range(n):
        for j in range(n):
            if bomb[i][j]=='*':
                output[i][j]='*'

for i in range(n):
    for j in range(n):
        #1. 지뢰가 없고, 열린경우
        if bomb[i][j]!='*' and open[i][j]=='x':
            output[i][j]=str(insertNum(i,j))
        if bomb[i][j]=='*' and open[i][j]=='x':
            insertbomb()

for i in range(n):
    test="".join(output[i])
    print(test)