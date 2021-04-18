def insert(arr):
    for i in range(1,len(arr)):
        j=i
        while j>0 and arr[j-1]>arr[j]:
            arr[j-1],arr[j]=arr[j],arr[j-1]
            j-=1
    return arr

arr=[4,5,3,1,6,2,7,10,13,8]
print(insert(arr))