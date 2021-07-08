# B989006 권오승
import math
def decimal(num):
    if num==1: # 1은 소수가 아니다
        return False
    for i in range(2, int(math.sqrt(num))+1): # 2부터 num의 제곱근+1까지(제곱근*제곱근=자기 자신이기 때문에 sqrt사용해 용랑 낮춤
        if num/i==1: # 자기 자신일때는 반복문 종료
            break
        elif num%i==0: # 1과 자기 자신을 제외하고 나눠지는 것은 소수가 아니다
            return False
    return True
n=int(input())
for i in range(1,n+1):
    if decimal(i)==True: # 소수인 경우에만 return True를 가지므로
        print(i)