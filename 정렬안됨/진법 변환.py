# 진법 변환(n 진수 -> 10 진수)
def convert(num, base): # 진법 변환을 위한 함수
    mul, result=1,0
    while num>0:
        result+=num%10*mul # 결과 값에 1의 자리 수*mul 을 해준다.
        mul*=base # 2진법일 경우 1, 2, 4, 8 ...
        num=num//10 # 앞의 자리를 하나씩 없앤다.
    return result

print("원하는 수를 입력하세요: ", end=' ')
n=int(input())
print("몇진법인가요?: ",end=' ')
base=int(input())
print(convert(n,base))