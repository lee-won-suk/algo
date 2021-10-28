def solution(routes):

    routes.sort()
    #겹치는 범위 정하기
    start,end=routes[0]
    #카메라 개수
    camera=0
    for i in range(1,len(routes)):
        #1. 안겹치는 경우
        if end<routes[i][0]:
            camera+=1
            start,end=routes[i]
        #2. 절반만 겹치는 경우 겹치는 범위로 변경해줌.
        elif  routes[i][0]<=end<=routes[i][1]:
            start=routes[i][0]
        else:
            start,end=routes[i]
    return camera+1

print( solution([[-20,-15], [-14,-5], [-18,-13], [-5,-3]]) )
