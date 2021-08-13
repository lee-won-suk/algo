from itertools import combinations_with_replacement

#N,M입력
N,M=map(int,input().split())
chicken=[ list(map(int,input().split()) ) for _ in range(N)]

#조합만들기
num=list( map(list , combinations_with_replacement(range(M),3) ) )

ans=0
#뽑은 치킨 종류 조합내에서 최대값 찾아보기
for i in range(len(num)):
    total=0
    for j in range(N):# 인원순서
        temp=0 # 1명의 선호도 최대값
        for a in num[i]:# 조합의 치킨 번호 추출
            temp=max(temp,chicken[j][a])
        total+=temp
    ans=max(ans,total)


print(ans)