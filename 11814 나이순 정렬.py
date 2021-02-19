n=int(input())
count=0
arr=[]
for _ in range(n):
    age,name=input().split()
    count+=1
    arr.append((age,name,count))
arr.sort(key=lambda x:(int(x[0]),x[2]))
for i,j,l in arr:
    print(i,j)