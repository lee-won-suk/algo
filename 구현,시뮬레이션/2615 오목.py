#2차원 배열 입력
omok=[ list(map(int,input().split() )) for _ in range(19) ]
#경계를 벗어나는지 여부 확인 함수
def edge(x,y):
    if x<19 and x>=0 and y<19 and y>=0:
        return True
    return False
# 이동배열 하,우하,우,우상
dx=[0,1,1,1]
dy=[1,1,0,-1]


def find_Omok():
    for i in range(19):
        for j in range(19):
            if omok[i][j]: #0이 아닐때
                for d in range(4):
                    x=j
                    y=i
                    cnt=1
                    while edge(x+dx[d],y+dy[d]) and (omok[i][j]==omok[y+dy[d]][x+dx[d]]):
                        x+=dx[d]
                        y+=dy[d]
                        cnt+=1
                    if cnt==5:
                        x=j
                        y=i
                        if edge(x-dx[d],y-dy[d]) and (omok[i][j] == omok[y - dy[d]][x - dx[d]]):
                            break
                        else:
                            return omok[i][j], i+1,j+1
    return 0,-1,-1
c,x,y=find_Omok()
if c!=0:
    print(c)
    print(x,y,sep=" ")
else:
    print(0)
