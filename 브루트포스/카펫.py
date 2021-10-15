def solution(brown, yellow):
    if yellow==1:
        return [3,3]
    for i in range(2,yellow+1):
        if yellow%i==0 and i>=(yellow//i) and (i+2)*2+(yellow//i)*2==brown:
            return[i+2,yellow//i+2]

def solution(brown, yellow):
    for i in range(1,int(yellow**0.5)+1):
        if yellow%i==0  and (i+yellow//i)*2==brown-4:
            return[yellow//i+2,i+2]




print(solution(24,24))
