

def solution(prices):
    from collections import deque
    q=deque(prices)
    answer = []
    while q:
        time=0
        tmp=q.popleft()
        if not q:
            answer.append(0)
            break
        for i in q:
            time += 1
            if tmp>i:
                break
        answer.append(time)
    return answer
'''

def solution(prices):
    answer = []
    while prices:
        time=0
        tmp=prices.pop(0)
        if not prices:
            answer.append(0)
            break
        li=list(filter(lambda x: prices[x]<tmp, range(len(prices))))
        if li:
            answer.append(li[0]+1)
        else:
            answer.append(len(prices))
    return answer
    '''
p=[1, 2, 3, 2, 3]
print(solution(p) )