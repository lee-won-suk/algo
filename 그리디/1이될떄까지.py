N=int(input())
X=list(map(int,input().split()))
X.sort(reverse=True)
group=0
pear=X[0]
man=0
for i in range(N-1):
    if pear==0:
        pear=X[i]
    if man==pear:
        group+=1
        pear=0
        man=0
    else:
        man+=1
if X[N-1]==1:
    group+=1
elif pear==man+1:
    group+=1
print(group)