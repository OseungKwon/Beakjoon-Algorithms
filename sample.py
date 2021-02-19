n=int(input())
arr=[]
for _ in range(n):
    age,name=input().split()

    arr.append((age,name))
arr.sort(key=lambda x:int(x[0]))
for i,j in arr:
    print(i,j)