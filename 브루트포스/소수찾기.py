
from itertools import permutations
def solution(n):
    a=set()
    for i in range(len(n)):
        # |= and 연산을 하고 합치는 연산이다. 1~n개 짜리 순열을 만든 후 join으로 붙임. 그다음int로 숫자화한다. 즉 모든 소수를 만드는
        #경우의 수를 가질 수 있음.
        a|=set(map(int, map("".join, permutations(list(n),i+1  ) )))

    a-=set(range(0,2))# 0,1 제거

    for i in range(2,int( max(a)**0.5)+1):  # 가장 큰 수의 제곱근까지만 구함
        a-=set(range(i*2,max(a)+1,i ))  # 2부터 그 수를 제외한 배수들을 전부 제거.
    return len(a)

a="011"
print(solution(a) )