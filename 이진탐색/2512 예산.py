from collections import Counter
import sys
input=sys.stdin.readline
#n입력
n=int(input())
money=Counter( map(int,input().split()))
m=int(input())
start,end=0,max(money)

while start<=end:
    mid=(start+end)//2
    total=0
    for value,cnt in money.items():
        if value<=mid:
            total+=value*cnt
        else:
            total+=mid*cnt
    #if total==m:
      #  break
    if total<=m:
        start=mid+1
    else:
        end=mid-1
print(end)