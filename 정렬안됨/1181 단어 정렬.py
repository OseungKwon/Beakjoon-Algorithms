n=int(input())
arr=[]
for _ in range(n):
    word=input()
    arr.append((word,len(word)))
arr=list(set(arr))
arr.sort(key=lambda x: (x[1],x[0]))
for i,j in arr:
    print(i)