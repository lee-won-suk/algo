import sys
input=sys.stdin.readline

#유클리드 호제법을 이용한 최대공약수
def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return a

# 최소공배수는 두수의 곱에서 최대공약수를 나누면 된다.
n=int(input())
order=list(map(int,input().split()))
g=  gcd( order[0] ,  gcd(order[1],order[-1])  )

for i in range(1,(g//2)+1):
    if g%i==0:
        print(i)
print(g)