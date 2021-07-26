#n입력
n=int(input())

calender=[[0]*366 for _ in range(n)]

todo=list()

for _ in range(n):
    #일정 입력받고 저장하기
    s ,e= map(int,input().split(' '))
    todo.append((s,e))

todo.sort(key=lambda x: (x[0], -x[1]))
# 시작일은 같은데 종료일이 더큰거 위치 변경하기

for k in range(len(todo)):
    s, e = todo[k][0], todo[k][1]

    for i in range(n):
        if 1 in calender[i][s: e + 1]:
            continue

        for j in range(s,e+1):
            calender[i][j] = 1
        break
#행 기억
row = 0
col = 0
ans = 0
# 정사각형 크기 구하기
for j in range(1,366):
    one_check=False
    for i in range(n):
        if calender[i][j] == 1:
            one_check = True
            row = max(row, i+1)
    if one_check:
        col+=1
    else:
        ans += row * col
        row = 0
        col = 0
if one_check:
     ans+= row * col

print(ans)
