#문자열 입력 받기
duckvoice=input()
#오리 개수 변수
count=0
#오리 울음소리 배열
voice=['q','u','a','c','k']
#오리 울음소리 인덱스
now=0
array=[False for _ in range( len(duckvoice) )]

# 추가 : 문자열이 5의 배수가 아닌것 제거
if len(duckvoice)%5!=0:
    print(-1)
    exit()

for i in range(len(duckvoice)):
    if duckvoice[i]=='q' and not array[i]:#첫시작을 q가 보이면 시작한다. 그리고 방문하지 않았어야한다.
        first=True # 이걸 쓰는 이유는 한 오리가 여러번 운걸 구분하기 위해서 쓴다.
        for j in range(i,len(duckvoice)): # 이건 다시 처음으로 돌아가서 조사할 필요없어서 i부터로 표현.
            if not array[j] and duckvoice[j]==voice[now]: # 현재 울음소리와 오리울음소리 순서가 같고,방문안했을 때
                array[j]=True #방문한걸로 표시
                if duckvoice[j]=='k': # k까지 울음소리 포착했을 때
                   if first: #아직 안셌으면 센다.
                        count += 1
                        first = False  # 한번 검사할 때 중복되서 찾은건 1번만 하려고
                   now = 0 #오리 울음소리 처음부터 다시 세기
                   continue #0번째로 초기화해서 +1안하려고
                now += 1

if not all(array) or count==0: # 문자열을 다방문하지 않았거나 오리가 1마리도 없을 때
    print(-1)
else:
    print(count)