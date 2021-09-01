#2개의 딕셔너리 사용해서 풀기
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
Pocket=dict()
for i in range(1,N+1):
    data=input().rstrip()
    Pocket[i]=data
   # Pocket[data]=i
revP=dict(map(reversed,Pocket.items()))

for i in range(M):
    data=input().rstrip()
    if data.isalpha():
        print(revP[data])
    elif data.isdigit():
        print(Pocket[int(data)])

'''    하나의 딕셔너리에서 뒤집은 key, value 쌍도 다 저장하기
import sys
input=sys.stdin.readline
N,M=map(int,input().split())
Pocket=dict()
for i in range(1,N+1):
    data=input().rstrip()
    Pocket[i]=data
    Pocket[data]=i


for i in range(M):
    data=input().rstrip()
    if data.isalpha():
        print(Pocket[data])
    elif data.isdigit():
        print(Pocket[int(data)])
'''