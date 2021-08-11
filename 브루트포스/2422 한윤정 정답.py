from itertools import combinations
import sys
input=sys.stdin.readline
#N, M 입력
N,M=map(int, input().split())
order=[[False]*(N+1) for _ in range(N+1)]
cnt=0

#조합 미리 만들기
iceCream=list(combinations(range(1,N+1),3))

for i in range(M):
    x,y=map(int,input().split())
    order[x][y]=True
    order[y][x] =True

for i in iceCream:
    if order[i[0]][i[1]] or order[i[1]][i[2]] or order[i[0]][i[2]]:
        continue
    cnt+=1
print(cnt)


