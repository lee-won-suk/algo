#n,m입력
while True:
    n,m=map(int,input().split())
    if n==0 and m==0:
        break
    dic={}
    arr=[list(map(int,input().split())) for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if arr[i][j] not in dic:
                dic[ arr[i][j] ]=1
            else:
                dic[arr[i][j]]+=1

    FirstPoint=max(dic.values())
    secondPoint=0
    for i in dic.values():
        if i< FirstPoint and i>=secondPoint:
            secondPoint=i
    total=[]
    for key in sorted(dic):
       if dic[key]==secondPoint:
           total.append(key)
    print(' '.join(map(str,total)  ))