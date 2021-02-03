def quick(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    low,high=list(),list()
    for i in range(1,len(arr)):
        if arr[i]<pivot:
            low.append(arr[i])
        else:
            high.append(arr[i])
    return quick(low)+[pivot]+quick(high)
n = int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
print("\n".join(str(i) for i in quick(arr)))

