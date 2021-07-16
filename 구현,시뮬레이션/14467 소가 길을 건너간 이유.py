#N입력
n=int(input())
#현재 길 위치배열
navi= [None for _ in range(11)]
#이동한 횟수 배열
count=[0]*11

for i in range(n):
    num, go=map(int,input().split())
    #navi의 현재 길 위치와 입력받은 go가 다른경우
    if navi[num]!=None and navi[num]!=go:
        #위치 갱신 및 카운트 증가
        navi[num]=go
        count[num]+=1
    else:
        navi[num] = go

total=0

print(sum(count))