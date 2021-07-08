def merge(arr):
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    low_arr = arr[:mid]
    high_arr = arr[mid:]
    merge(low_arr)
    merge(high_arr)

    l = h = fin = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            arr[fin] = low_arr[l]
            l += 1
        else:
            arr[fin] = high_arr[h]
            h += 1
        fin += 1
    if h == len(high_arr):
        while l < len(low_arr):
            arr[fin] = low_arr[l]
            l += 1
            fin += 1
    elif l == len(low_arr):
        while h < len(high_arr):
            arr[fin] = high_arr[h]
            h += 1
            fin += 1
    return arr


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
merge(arr)
for i in merge(arr):
    print(i)
