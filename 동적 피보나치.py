num = int(input())

def fibo(n):
    zero = [1, 0]
    one = [0, 1]
    if len(zero) <= n:
        for i in range(2,n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print(zero[n], one[n])

for i in range(num):
    fibo(int(input()))