def hanoi(n,a,b,c):
    if n==1:
        result.append([a,c])
    else:
        hanoi(n-1,a,c,b)
        result.append([a,c])
        hanoi(n-1,b,a,c)
result=[]
hanoi(int(input()),1,2,3)
print(len(result))
print("\n".join([' '.join(str(i3) for i in row)for row in result]))