#버블 정렬
def bubble(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
bubble(arr)
for i in range(n):
    print(arr[i])