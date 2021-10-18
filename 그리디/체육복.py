def solution(n, lost, reserve):
    a=list(set(lost)&set(reserve))
    for i in a:
        lost.remove(i)
        reserve.remove(i)
    lost.sort()
    reserve.sort()
    n -= len(lost)
    for i in lost:
        for j in reserve:
            if j==i-1 or j==i+1:
                reserve.pop(0)
                n+=1
                break
    return n

print(solution(5,[2,4], [3] ))