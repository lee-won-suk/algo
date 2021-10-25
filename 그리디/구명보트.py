# def solution(people, limit):
#     boatCnt=0
#     people.sort()
#     while people:
#         idx1=people.pop(0)
#         for i in range(len(people)-1,-1,-1):
#             if idx1+people[i]<=limit:
#                 people.pop(i)
#                 break
#         boatCnt += 1
#     return boatCnt

def solution(people, limit):
    from collections import deque
    boatCnt=0
    people.sort()
    p=deque(people)
    while p:
        if len(p)>=2:
            if p[0]+p[-1]<=limit:
                p.popleft()
            p.pop()
            boatCnt += 1
        else:
            p.pop()
            boatCnt+=1
    return boatCnt



solution2([30,40,70, 50, 80, 50],100)
