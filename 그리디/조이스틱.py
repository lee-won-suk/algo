def solution(name):

    answer=0
    min_left_right=len(name)-1
    next_idx=0
    for i,char in enumerate(name):
        answer+=min(ord(char)-ord('A'),ord('Z')-ord(char)+1)

        next_idx=i+1
        while next_idx<len(name) and name[next_idx]=='A':
            next_idx+=1
        min_left_right=min(min_left_right,i+i+len(name)-next_idx)

    return answer+min_left_right

