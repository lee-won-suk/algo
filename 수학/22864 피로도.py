A,B,C,M=map(int,input().split())
p=0
work=0
for _ in range(24):
    if p+A<=M: #일할 수 있으면
        p+=A
        work+=B
    else:
        if p-C<0:
            p=0
        else:
            p-=C
print(work)