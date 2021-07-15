import math
#입력
n=int(input())
#n2이하 자연수
num=int(input())
numx=0
numy=0

#가변하는 범위 변수
level=1
array=[[0]*n for _ in range(n)]

#이동을 위한 배열
#현재 이동방향도
dx=[-1,0,1,0]
dy=[0,1,0,-1]

now=0
#시작 좌표
startx=n//2
starty=n//2
#현재 좌표
nx=ny=n//2
array[nx][ny]=1
#이동해야될 다음좌표 함수

#제곱수
squareNum=3
def move(x,y,n):
    #현재 방향을 기준으로 1. 밖으로 벗어나면 방향 변경해서 반영 2.안나가면 계속
    global now,nx,ny,dx,dy
   # print("1.xy"+str(x)+str(y))
    kx = x + dx[now]
    ky = y + dy[now]
   # print("2.kxky="+str(kx)+str(ky))
    if kx>=0 and ky>=0 and (0<= abs( abs (kx)  - startx  )<=level) and  (0<=abs( abs(ky) - starty)  <=level):
        nx=kx
        ny=ky
        return [kx,ky]

    else:
        if now!=3:
            now+=1
        else:
            now=0
        nx = x + dx[now]
        ny = y + dy[now]
        return [nx,ny]


for i in range(2,n*n+1):
    #다음 인덱스 구하기
    arr=move(nx,ny,n)
    #print("3.arr"+str(arr[0])+str(arr[1]))
    array[nx][ny]=i
    #print("4.i="+str(i))
    if  int(math.sqrt(i) )==squareNum:
        level+=1
        squareNum+=2
       # print("level변경 "+str(level))

    if num==1:
        numx=(n-1)//2
        numy=(n-1)//2
    elif num==i:
        numx=nx
        numy=ny

for i in range(n):
    print(' '.join(map(str,array[i]) ) )

print(numx+1,numy+1,sep=" ")