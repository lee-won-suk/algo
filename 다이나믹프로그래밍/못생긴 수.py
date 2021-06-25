#1. 몇번째 못생긴 수인지 입력받기
n=int(input())
#테이블 만들기
ugly=[0]*n
ugly[0]=1#첫번째 수는 1

#2,3,5배 인덱스
i2=i3=i5=0

#초기 곱셈값
next2,next3,next5=2,3,5


for i in range(1,n):
    ugly[i]=min(next2,next3,next5)

    if ugly[i]==next2:
        i2+=1
        next2=ugly[i2]*2
    if ugly[i] == next3:
        i3 += 1
        next3 = ugly[i3] * 3
    if ugly[i] == next5:
        i5 += 1
        next5 = ugly[i5] * 5

print(ugly[n-1])