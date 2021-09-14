N=int(input())
cnt=0
for _ in range(N):
    word=input().rstrip()
    if list(word)== sorted(word,key=word.find):
        cnt+=1
print(cnt)