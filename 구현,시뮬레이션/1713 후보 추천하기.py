from collections import deque
#N 입력
n=int(input())
#총추천 리스트
Total_Suggest=int(input())
#추천학생 리스트
suggest_list=list(map(int, input().split()))
suggest_num=[0]*101
#사진틀 큐
picture=deque()

for number in suggest_list:

    suggest_num[number] += 1
    #사진틀에 없으면
    if number not in picture:
        #꽉차있을 경우
        if len(picture)==n:
            num=picture[0]
            #추천수 제일적은거 찾기
            for a in picture:
                if suggest_num[num]>suggest_num[a]:
                    num=a
            picture.remove(num)
            suggest_num[num]=0
        picture.append(number)
picture=sorted(picture)
print(' '.join(map(str,picture)))