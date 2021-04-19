
a=input()
result=int(a[0])#첫숫자는 바로 넣어준다.

for i in range(len(a)):
   num=int(a[i])

   if num<=1 or result<=1:
      result+=num
   else:
      result*=num

print(result)