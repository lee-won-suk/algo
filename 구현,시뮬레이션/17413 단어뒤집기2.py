#s입력
s=list(input())
i=0
start=0
while i<len(s):
    if s[i]=='<':
        while s[i]!=">":
            i+=1
        i+=1 #닫힌 괄호시 +1
    elif s[i].isalnum():#숫자나 알파벳이면
        start=i
        while i<len(s) and s[i].isalnum():
            i+=1
        revs=s[start:i]
        revs.reverse()
        s[start:i]=revs
    else:
        i+=1
print("".join(s))