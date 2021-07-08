def merge(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    low = merge(arr[:mid])
    high = merge(arr[mid:])

    merged = []
    l = h = 0
    while l < len(low) and h < len(high):
        if low[l] < high[h]:
            merged.append(low[l])
            l += 1
        else:
            merged.append(high[h])
            h += 1
    merged += low[l:]
    merged += high[h:]
    return merged

arr=[4,5,3,1,6,2,7,10,13,8]
print(merge(arr))
