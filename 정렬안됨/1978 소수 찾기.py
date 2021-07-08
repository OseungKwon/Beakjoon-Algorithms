size=int(input())
num=list(map(int,input().split()))
count=0
x=max(num)
arr=[]
for i in range(x+1):
    if(i>=2):
        arr.append(i)
           
for i in range(len(arr)):
    if(arr[i]!=0):
        for j in range(i+1,len(arr)):
            if(arr[i]!=0):
                if(arr[j]%arr[i]==0):
                    arr[j]=0
                    
for i in num:
    if i==1:
        pass
    elif(arr[i-2]==i):
        count+=1
print(count)
