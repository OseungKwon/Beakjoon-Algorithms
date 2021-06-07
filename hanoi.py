def hanoi(n,frm,to,otr):
    if n==1:
        print(frm,to)
        return
    hanoi(n-1,frm,otr,to)
    print(frm,to)
    hanoi(n-1,otr,to,frm)

n=int(input())
print((2**n)-1)
hanoi(n,1,3,2)
