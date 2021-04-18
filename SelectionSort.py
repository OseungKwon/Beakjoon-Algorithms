def selection(arr):
    length=len(arr)
    for i in range(length-1):
        min_j=i
        for j in range(i+1,length):
            if arr[min_j]>arr[j]:
                min_j=j
            arr[i],arr[min_j]=arr[min_j],arr[i]
    return arr

arr=[4,5,3,1,6,2,7,10,13,8]
print(selection(arr))