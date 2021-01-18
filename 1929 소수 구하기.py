m,n=map(int,input().split())
arr=[]
for i in range(2,n+1):
    arr.append(i)
for i in range(len(arr)):
    if(arr[i]!=0):
        for j in range(i+1,len(arr)):
            if(arr[j]%arr[i]==0):
                arr[j]=0;
for i in arr[m-2:]:
    if(i!=0):
        print(i)
