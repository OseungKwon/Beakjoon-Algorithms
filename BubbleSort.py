def bubble(arr):
    length=len(arr)-1
    for num in range(length,0,-1):
        for i in range(num):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr

arr=[4,5,3,1,6,2,7,10,13,8]
print(bubble(arr))