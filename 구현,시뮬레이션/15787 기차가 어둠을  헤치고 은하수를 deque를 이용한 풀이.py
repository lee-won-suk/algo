from collections import deque
import sys
n,m=map(int,input().split())
train=[ deque([0]*20) for _ in range(n)] # deque로 만들기
for i in range(m):
    op=list(map(int,input().split()))
    if op[0]==1:
        train[op[1]-1][op[2]-1]=1
    elif op[0] == 2:
        train[op[1] - 1][op[2] - 1] = 0
    elif op[0] == 3:
        train[op[1] - 1].rotate(1) #오른쪽으로 1씩 이동하고 0번째 제거
        train[op[1]-1][0]=0
    else:
        train[op[1] - 1].rotate(-1) # 왼쪽으로 1씩 이동하고 마지막좌석 제거
        train[op[1] - 1][19] = 0
answer=[]
for i in train:
    if i not in answer: # 중복이 안되는 열차 배치도만 고르는 로직
        answer.append(i)
print(train)
print(answer)