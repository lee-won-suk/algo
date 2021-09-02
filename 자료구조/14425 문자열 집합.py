import sys
input=sys.stdin.readline
N,M=map(int,input().split())

S=set()
cnt=0
for i in range(N):
    S.add(input().rstrip())

for i in range(M):
    data=input().rstrip()
    if data in S:
        cnt+=1

print(cnt)