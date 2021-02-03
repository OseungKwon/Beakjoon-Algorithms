def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[min_index]:
                min_index=j;
        arr[i], arr[min_index]=arr[min_index],arr[i]

n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))

selection_sort(arr)
for i in range(n):
    print(arr[i])