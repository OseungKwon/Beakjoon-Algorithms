n = int(input())
arr = [0]*n

for i in range(n):
    arr[i]=list(map(int, input().split()))
arr=sorted(arr)
for i in range(n):
    print(arr[i][0],arr[i][1])
