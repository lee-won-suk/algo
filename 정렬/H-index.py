def solution(citations):
    h=0
    citations.sort(reverse=True)
    while True:
        cnt = 0
        # h번 이상 인용된 논문개수 세기
        for i in citations:
            if i>=h: cnt+=1
            else: break
        #인용된 논문개수가 h편이상이면 H-INDEX갱신
        if cnt>=h: h+=1
        elif cnt<h:
            h-=1
            break
    return h
from collections import Counter
def solution(citations):
    citations.sort(reverse=True)
    return max(map(min,enumerate(citations,start=1)))



c=[3, 0, 6, 1, 5]
c.sort(reverse=True)

#[(1, 6), (2, 5), (3, 3), (4, 1), (5, 0)]

#print(solution(c))