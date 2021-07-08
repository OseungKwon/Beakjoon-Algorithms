def calc(n):
    arr=[True]*n
    m=int(n**0.5)
    for i in range(2, m+1):
        if arr[i]==True:
            for j in range(i+i, n, i):
                arr[j]=False
    return [i for i in range(2, n) if arr[i]==True]

def sum(n):
    li=calc(n)
    num=max([i for i in range(len(li)) if li[i] <= n/2])
    for i in range(num, -1, -1):
        for j in range(len(li)):
            if li[i] + li[j] == n:
                return [li[i], li[j]]
T=int(input())
for _ in range(T):
    n=int(input())
    print(*sum(n))
