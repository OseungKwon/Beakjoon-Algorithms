#삽입 정렬
def insertion(arr):
    for end in range(1, len(arr)):
        for i in range(end,0,-1):
            if arr[i]<arr[i-1]:
                arr[i],arr[i-1]=arr[i-1],arr[i]
n=int(input())
arr=[]
for _ in range(n):
    arr.append(int(input()))
insertion(arr)
for i in range(n):
    print(arr[i])