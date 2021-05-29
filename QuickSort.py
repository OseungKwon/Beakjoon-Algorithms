def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    low, equal, high = [], [], []
    for num in arr:
        if num < pivot:
            low.append(num)
        elif num > pivot:
            high.append(num)
        else:
            equal.append(num)
    return quick_sort(low) + equal + quick_sort(high)

arr=[4,5,3,1,6,2,7,10,13,8]
print(quick_sort(arr))
