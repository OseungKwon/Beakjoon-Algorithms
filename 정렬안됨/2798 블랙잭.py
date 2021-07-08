n,m=map(int,input().split())
arr=list(map(int,input().split()))
b=len(arr)
sum=0
for i in range(0,b-2):
    for j in range(i+1,b-1):
        for k in range(j+1,b):
            if arr[i]+arr[j]+arr[k]>m:
                continue
            else:
                    sum=max(sum,arr[i]+arr[j]+arr[k])
print(sum)