import math

n=1000
array=[True for i in range(n+1) ]
array[1]=False#1은 소수가 아니므로

for i in range( 2, int( math.sqrt(n))+1  ):
    if array[i]==True:
        j=2
        while i*j<=n:
            array[i*j]=False
            j+=1

for i in range(2,n+1):
    if array[i]:
        print(i,end=' ')