def merge(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low_arr = merge(arr[:mid])
    high_arr = merge(arr[mid:])

    merged = []
    l = h = 0
    while l < len(low_arr) and h < len(high_arr):
        if low_arr[l] < high_arr[h]:
            merged.append(low_arr[l])
            l += 1
        else:
            merged.append(high_arr[h])
            h += 1

    merged += low_arr[l:]
    merged += high_arr[h:]
    #print("merge: ", merged)
    #print("low", l, low_arr[l:], end="\t")
    #print("high", h, high_arr[h:])
    return merged


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
merge(arr)
for i in merge(arr):
    print(i)
