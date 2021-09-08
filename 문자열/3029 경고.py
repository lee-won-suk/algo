#두 시간 입력
first=input()
last=input()
h,m,s=0,0,0
s=int(last[6:])-int(first[6:])
m = int(last[3:5]) - int(first[3:5])
h=int(last[0:2])-int(first[0:2])
if s<0:
    s+=60
    m-=1
if m < 0:
    m += 60
    h -= 1
if h<0: h+=24

if h==m==s==0:
    h=24
h=format(h,'02')
m=format(m,'02')
s=format(s,'02')

print(h,m,s,sep=':')
