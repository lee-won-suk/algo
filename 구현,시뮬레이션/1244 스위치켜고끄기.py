
#n 입력받기 (스위치개수
n=int(input())
#스위치 상태 입력받기
arr=list(map(int,input().split()))
#학생수 입력
stu=int(input())

#상태 변경 함수
def chanceSwitch(gender,num):  #xor활용
    if gender==1:
        i = 1
        while num*i-1 <=n-1:
            arr[ num*i-1 ]^=1
            i+=1

    else:
    #받은 번호 중심으로 스위치가 대칭인곳까지 변경
        arr[num-1]^=1
        arrnum=1
        while num-1-arrnum>=0 and num-1+arrnum<n :
            if arr[num-1-arrnum]==arr[num-1+arrnum]:
                arr[num-1-arrnum]=arr[num-1+arrnum]=arr[num-1+arrnum]^1
                arrnum+=1
            else:
                break

for i in range(stu):
    gender,num=map(int,input().split())
    chanceSwitch(gender,num)


for i in range( len(arr)):

    print(arr[i] , end=" ")
    if i!=0 and (i+1)%20==0:
        print()