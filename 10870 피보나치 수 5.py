def fibo(x):
    if x<=1:
        return x
    return fibo(x-1)+fibo(x-2)

n=int(input())
print(fibo(n))