def counting_arr(arr,K):
    n=len(arr)
    output=[0]*n
    count=[0]*K

    for i in arr:
        count[i]+=1
    for i in range(1,K):
        count[i]+=count[i-1]

    for i in range(len(arr)):
        output[count[arr[i]]-1] = arr[i]
        count[arr[i]] -= 1

    return output

arr = [ 3, 5, 1, 1, 2, 9, 7, 6, 4, 7, 5 ]
print(counting_arr(arr, max(len(arr),max(arr))))