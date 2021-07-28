# H , W입력
H,W=map(int,input().split())

cloudArr=[input() for _ in range(H) ]


ansArr=[ [0]*W for _ in range(H) ]
isCloud=False
cnt=1


for i in range(H):
    isCloud=False
    cnt=1
    for j in range(W):
        #1 isCloud가 false면서 .일때
        if isCloud==False and cloudArr[i][j]=='.':
            ansArr[i][j]=-1
        #2. 구름일 때
        if cloudArr[i][j]=='c':
            isCloud=True
            cnt=1
        #3. 앞에 구름이 있을 때 .이면
        elif isCloud==True and cloudArr[i][j]=='.':
            ansArr[i][j]=cnt
            cnt+=1

for i in range(H):
    print(" ".join( map(str, ansArr[i] )   ) )
