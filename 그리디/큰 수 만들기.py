


def solution(number,k):
    stack=[]
    for elem in number:
#stack이 안비어있고, 마지막원소가 현재 숫자보다 작고,k가0이상이면
        while stack and stack[-1]<elem and k>0:
            stack.pop() #마지막원소를 뺀다.
            k-=1
        stack.append(elem)

    #k가 남았을 경우: 남은만큼 어떻게든 빼줘야할 때. 뒤에서부터 제거.
    stack=stack[:-k] if k>0 else stack
    answer=''.join(stack)
    return answer
