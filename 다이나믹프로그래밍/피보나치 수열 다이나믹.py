#메모이제이션을 위한 리스트 초기화
d=100*[0]

#피보나치를 재귀함수로 구현 (탑다운 )
def fibo(x):
    #1이나 2일떄
    if x==1 or x==2:
        return 1
    #계산한적 있는 경우
    if d[x]!=0:
        return d[x]
    #아직 계산하지 않은 문제-> 점화식 사용
    d[x]=fibo(x-1)+fibo(x-2)
    return d[x]
#바텀업 방식
x=[0]*100
x[1]=1
x[2]=1
n=99
for i in range(3,n+1):
    x[i]=x[i-2]+x[i-1]
print(x[n])



#바텀업 방식
print(fibo(99))