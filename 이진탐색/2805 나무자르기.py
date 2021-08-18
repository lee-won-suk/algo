import sys
#n,m 입력
n,m=map(int,sys.stdin.readline().split())
tree=list(map(int , sys.stdin.readline().split()  ))

#시작값과 끝값 지정
start,end=1,max(tree)

while start<=end:
    mid=(start+end)//2
    #벌목된 나무 총합
    total=0
    for i in tree:
        if i>=mid:
            total+=i-mid

    #벌목 높이 탐색하기
    if total>=m:
        start=mid+1
    else:
        end=mid-1
print(end)






'''
H=1
total=sum(tree)
while total-H*n!=m:
    if total-H*n<m:
        H-=1
    else:
        H+=1

print(H)
'''
