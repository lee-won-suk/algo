import math

# n과 m 입력
n,m=map(int,input().split())
arr=[0]*(n+1)
for i in range(n+1):
    arr[i]= math.factorial(i)

a=arr[n]//(arr[n-m]*arr[m])
print(a)