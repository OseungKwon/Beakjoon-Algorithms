def fibo(n):
    if n<=2:
        if n==0:
            return 0
        return 1
    return fibo(n-1)+fibo(n-2)
print(fibo(int(input())))