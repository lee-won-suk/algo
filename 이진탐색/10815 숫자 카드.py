import sys

n=int(input())
num=list(map(int,sys.stdin.readline().split() ))
m=int(input())
find= list(map(int,sys.stdin.readline().split() ))
num.sort()


def binarySearch(arr,search,start,end):

    while start<=end:
        mid = (start + end) // 2

        if arr[mid]==search:
            return mid
        if arr[mid]>search:
            end=mid-1
        else:
            start = mid + 1
    return None

for i in range(m):
    if binarySearch(num,find[i],0,n-1) is not None:
        print(1,end=' ')
    else:
        print(0,end=' ')


'''
def bs(arr,start):

    if len(arr)==1:
        if arr[0]==start:
            return 1
        else:
            return 0
    if len(arr)==0:
        return 0

    medium=len(arr)//2

    if num[medium]==start:
        return 1

    if  num[medium]>start:
        return bs(num[:medium],start)
    else:
        return bs(num[medium:],start)
for i in range(m):
    if i==m-1:
        print(bs(num,find[i]))
    else:
        print(bs( num , find[i]  ) ,end=' ' )
'''