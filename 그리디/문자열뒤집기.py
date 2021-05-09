a=input()
now=a[0]
count=0
for i in range(len(a)):
    if a[i]!=now:
        now=a[i]
        count+=1

if count %2 ==0:
    print(int(count/2))
else:
    print( int((count+1)/2))
