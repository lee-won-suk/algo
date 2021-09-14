import sys
input=sys.stdin.readline
N=int(input())
arr=set()
for i in range(N):
    arr.add(input().rstrip())
arr=list(arr)
arr.sort(key=lambda x :( len(x),x) )
print("\n".join(arr))


