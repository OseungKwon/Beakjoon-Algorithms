def chart(n):
    info = [[0] * 2 for _ in range(n)]
    arr = [1] * n
    for i in range(n):
        info[i] = list(map(int, input().split()))
    for i in range(n):
        for j in range(n):
            if info[i][0] > info[j][0] and info[i][1] > info[j][1]:
                arr[j] += 1
    return arr


n = int(input())
for i in chart(n):
    print(i)
