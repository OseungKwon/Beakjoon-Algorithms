n, m = map(int, input().split())
arr = list(map(int, input().split()))
max_m = 0
for i in range(0, n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if arr[i]+arr[j]+arr[k] <= m:
                max_m = max(max_m, arr[i]+arr[j]+arr[k])
print(max_m)

