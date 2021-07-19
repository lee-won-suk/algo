#빙고 배열 입력
bingo,check=[] , []
choose=[ [0]*5 for i in range(5)]
cnt=0
for i in range(5):
    bingo.append(list(map(int,input().split() ))   )
#빙고 체크하기
for i in range(5):
    check.append(list(map(int,input().split() ))   )



def bingocheck():
    count=0
    #1. 가로빙고
    for i in range(5):
        for j in range(5):
            if choose[i][j]==0:
                break
            elif choose[i][j]==1 and j==4:
                count+=1
    #2.세로빙고
    for i in range(5):
        for j in range(5):
            if choose[j][i] ==0:
                break
            elif choose[j][i]==1 and j==4:
                count+=1
     # 3.대각빙고
    for i in range(5):
        if choose[i][i] == 0:
            break
        elif choose[i][i] == 1 and i == 4:
            count += 1
    for i in range(5):
        if choose[i][4-i] == 0:
            break
        elif choose[i][4-i] == 1 and i == 4:
            count += 1
    return count

# choose에 사회자의 수 부분에 체크
def insertbingo(a,b):
    for i in range(5):
        for j in range(5):
            if bingo[i][j]==check[a][b]:
                choose[i][j]=1

for i in range(5):
    for j in range(5):
        #1개씩 체크
        cnt+=1
        insertbingo(i,j)
        test=bingocheck()
        if test >=3:
            print(cnt)
            exit(0)


