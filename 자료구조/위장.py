def solution(clothes):
    #개수 카운팅하기
    temp={}
    answer=1
    for i in clothes:
        if i[1] in temp:
            temp[i[1]]+=1
        else:
            temp[i[1]]=1
    for i in temp.values():
        answer*=(i+1)
    print(answer)
    return answer-1
def solution2(clothes):
    from collections import Counter
    from functools import reduce
    #Counter를 사용하면 딕셔너리 형태로 개수 구할 수 있음
    temp=Counter(kind for name,kind in clothes)

    #함수를 반복실행한 값을 구할 때 사용하는데.
    #아무것도 선택안하는 경우가지 포함해서(y+1)씩 곱해주고 전부선택안하는 경우 -1로 처리해줌.
    answer=reduce(lambda x,y:x*(y+1) ,temp.values(),1   )-1
    return answer

a=[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution2(a))