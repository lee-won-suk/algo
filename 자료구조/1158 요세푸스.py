from collections import deque
n,k=map(int,input().split())
num=deque( i for i in range(1,n+1))
ans=[]
while num:
    num.rotate(-k+1)
    ans.append(num.popleft())

print("<", end='')
for i in range(n):
    if i==n-1:
        print(ans[i],end="")
    else:
        print(ans[i],end=", ")

print(">", end='')