def solution(array, commands):
    answer = []
    for i,j,k in commands:#order in commands:
        #i,j,k=order[0],order[1],order[2]
        temp=sorted(array[i-1:j])
        answer.append(temp[k-1])
    return answer

a,c=[1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(a,c))