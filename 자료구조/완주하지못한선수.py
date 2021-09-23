
def solution(participant, completion):

    a,b=dict(),dict()
    hash_key=0#해쉬키
    #해쉬를 생성하면서 모든 키값들을 더함.
    #이러면 중복이라도 키값이 하나 남는다.
    for i in participant:
        a[hash(i)]=i
        hash_key+=hash(i)
        #두번째 해쉬를 생성하면서 미완주자를 제외하고 키값을 제거
    for i in completion:
        b[hash(i)] = i
        hash_key -= hash(i)
    return a[hash_key]
    # for i in participant:
    #     if pd[i]!=cd[i] or cd[i]==None:
    #         answer=i
    #         return answer

from collections import Counter
def solution(participant, completion):

    ans=Counter(participant)-Counter(completion)
    return list(ans.keys())[0]



a=['a','b','c']
b=['a','b','c','d']
ans=solution(b,a)
print(ans)

