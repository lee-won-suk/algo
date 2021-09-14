import sys
moum=['a','e','i','o','u']
input=sys.stdin.readline
while True:
    word=input().rstrip()
    if word=="end":
        break
    past=''
    za_cnt=0
    mo_cnt=0
    mo_flag=False
    flag=False
    for i in range(len(word)):
        if word[i] in moum:
            mo_cnt+=1
            mo_flag=True
            za_cnt=0
        else:
            mo_cnt=0
            za_cnt+=1
        if  word[i]==past and word[i]!='e' and word[i]!='o' or  (mo_cnt==3 or za_cnt==3)     :
            print("<"+word+"> is not acceptable.")
            flag=True
            break
        past=word[i]

    if flag==False:
        if mo_flag==False:
            print("<" + word + "> is not acceptable.")
        else:
            print("<" + word + "> is acceptable.")
