
def DM(k):
    if k==0:
        return 0
    elif k==1:
        return 1
    elif k%2==1:
        return 1-DM(k-1)
    else:
        return DM(k//2)
K=int(input())
x='0'
print(DM(K-1))

