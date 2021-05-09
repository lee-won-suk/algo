num=int(input())
data=list(map(int, input().split(" ")))

data.sort()
target=1

for i in data:
    if target<i:
        break
    target+=i

print(target)
#풀이 전략
'''
target을 처음에 1로 두고, 입력받은 숫자들과 비교해서 그숫자들을 더해가며 타겟을 업데이트한다.

1~ target-1까지 만들수 있는 상황일 때, target을 만들 수 있는지 판단한다.

'''