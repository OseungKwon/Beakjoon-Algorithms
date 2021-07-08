num=int(input())
def fibo(n):
    one=[0,1]
    if len(one) <= n:
        for i in range(2,n+1):
            one.append(one[i-1]+one[i-2])
    print(one)

fibo(num)