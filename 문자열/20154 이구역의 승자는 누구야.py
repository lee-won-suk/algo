numConvert=[3,2,1,2,3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]
#ord('A')-65 = 인덱스 번호
arr=input()
num=[]
#획으로 변환
for i in range(len(arr)):
    num.append( numConvert[ int(ord(arr[i])-65) ] )

result=sum(num)%10

if result%2==0:
    print("You're the winner?")
else:
    print("I'm a winner!")