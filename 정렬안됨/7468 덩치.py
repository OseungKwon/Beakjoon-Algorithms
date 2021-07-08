n=int(input())
A=[]
B=[1]*n
for _ in range(n):
    A.append(list(map(int,input().split())))

for i in range(0,n):
    for j in range(0,n):
        if A[i][0]<A[j][0] and A[i][1]<A[j][1]:
            B[i]+=1
for i in range(len(B)):
    print(B[i],end=' ')
