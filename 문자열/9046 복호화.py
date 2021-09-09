from collections import defaultdict
T=int(input())


for i in range(T):
    cnt = 0
    word=input()
    #처음 인자값이 들어와도 0으로 초기화되서 입력가능하게 defaultdict사용
    wordlist=defaultdict(int)
    #딕셔너리에 빈도수 계산
    for j in range(len(word)):
        if word[j]!=' ':
            wordlist[word[j]]+=1
    #가장 빈도수가 높은 값 가져옴.
    Mxnum=max(wordlist.values())
    for key,value in wordlist.items():
        #빈도수가 가장 높은 키값을 가져온다.
        if value==Mxnum:
            Mxkey=key
            cnt+=1

    if cnt>=2:
        print('?')
    else:
        print(Mxkey)
    cnt=0