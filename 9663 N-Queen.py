n=int(input())
arr=[]
def available(x,col):

    row=len(x)
    for queen_row in range(row):
        if x[queen_row]==col or abs(x[queen_row]-col)==row-queen_row:
            return False
    print(x,col,row)
    return True



def DFS(n,row,x,arr):
    if row==n:
        arr.append(x[:])
        #print(arr)
        return
    for col in range(n):
        if available(x,col):
            x.append(col)
            DFS(n,row+1,x,arr)
            x.pop()
DFS(n,0,[],arr)
print(len(arr))