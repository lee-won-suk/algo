import sys
#n 입력
n=int(input())
#파일 확장자 저장
file={}

for i in range(n):
    a=input().split('.')[1]
    if a not in file:
        file[a]=1
    else:
        file[a]+=1
file=sorted(file.items())

for i in range(len(file)):
    print( file[i][0],file[i][1] ,sep=" "  )