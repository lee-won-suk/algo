import math

def is_prime_number(x):
    #2부터 제곱근까지 검사
    for i in range(2,int(math.sqrt(x))+1):
        if x%i ==0:
            return False # 소수가 아님
    return True #소수임
