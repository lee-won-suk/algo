n=int(input())
arr=[list(map(int,input().split())) for _ in range(n)]
white,blue=0,0

def recursiveDC(y,x,n):
    global white,blue
    #첫 컬러 지정.
    color=arr[y][x]
    check=True

    for i in range(y,y+n):
        #이미 어긋난 숫자가 있어서 뒤까지 살피는건 무의미. 그래서 for문 탈출
        if not check:
            break
        for j in range(x,x+n):
            if color!=arr[i][j]:
                check=False
                recursiveDC(y,x,n//2)#1사분면
                recursiveDC(y,x+n//2, n//2  )#2사분면
                recursiveDC(y+n//2,x, n//2)#3사분면
                recursiveDC(y+n//2 , x+n//2, n//2)#4사분면
                break
    if check:
        if color==1:
            blue+=1
        else:
            white+=1


recursiveDC(0,0,n)
print(white)
print(blue)
