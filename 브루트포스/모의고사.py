def solution(answers):
    n1=[1,2,3,4,5]
    n2=[2,1,2,3,2,4,2,5]
    n3=[3,3,1,1,2,2,4,4,5,5]
    c1,c2,c3=0,0,0# 맞춘개수
    answer=[]
    for i in range(len(answers)):
        if n1[i%5]==answers[i]: c1+=1
        if n2[i%8]==answers[i]: c2+=1
        if n3[i%10]==answers[i]: c3+=1
    t=max(c1,c2,c3)
    if c1==t: answer.append(1)
    if c2==t: answer.append(2)
    if c3==t: answer.append(3)
    return answer

from itertools import cycle
def solution2(answers):
    arr=[
        cycle([1,2,3,4,5]),
        cycle([2, 1, 2, 3, 2, 4, 2, 5]),
        cycle([3, 3, 1, 1, 2, 2, 4, 4, 5, 5])
    ]
    score=[0,0,0]
    for num in answers:
        for j in range(3):
            if next(arr[j])==num:
                score[j]+=1
    highest=max(score)

    return [ i+1  for i,v in enumerate(score) if v==highest     ]


a=[1,3,2,4,2]
print(solution2(a))