#1025 : [기초-입출력] 정수 1개 입력받아 나누어 출력하기(설명)
a=list(map(int,input()))
num=4
for i in range(len(a)):
   print("["+str(a[i]*(10**num))+"]")
   num-=1
