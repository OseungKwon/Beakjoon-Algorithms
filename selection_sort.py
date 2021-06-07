# B989006 권오승
def selection(arr):
    for i in range(len(arr)-1):
        min=i # 임시 최소 인덱스 설정
        for j in range(i+1,len(arr)):
            if arr[min]>arr[j]: #최소값보다 arr[j]가 작으면
                min=j
        arr[i], arr[min]=arr[min],arr[i] #arr[i] 와 arr[min] 값 교환
    return arr
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
selection(arr)
print(arr)