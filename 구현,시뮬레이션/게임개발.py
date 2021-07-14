#맵 생성
n,m=map(int,input().split())
#방문한 위치 저장 맵
d=[[0]*m for _ in range(n)]
#현재 캐릭터, 위치 방향
x,y,direction=map(int,input().split())
d[1][1]=1 # 현재 좌표 방문처리

#맵정보
array=[]
for _ in range(n):
    array.append(list(map(int,input().split()))      )

#북동남서
dx=[-1,0,1,0]
dy=[0,1,0,-1]

#왼쪽회전
def turn_left():
    global direction# 전역변수 선언
    direction-=1
    if direction==-1:
        direction=3

count=1
turn_time=0
while True:
   turn_left()
   nx=x+dx[direction]
   ny=y+dy[direction]
   #가보지 않은 칸 존재시 이동
   if d[nx][ny]==0 and array[nx][ny]==0:
       d[nx][ny]=1
       x=nx
       y=ny
       count+=1
       turn_time=0
       continue
   #회전 후에 정면에 가보지 않은 칸이 없거나 바다인경우
   else:
       turn_time+=1
   #4방향 모두 갈 수 없는 경우
   if turn_time==4:
       nx=x-dx[direction]
       ny=y-dy[direction]
       #뒤로 갈 수 있으면 이동
       if array[nx][ny]==0:
           x=nx
           y=ny
       else:
           break
       turn_time=0
print(count)
