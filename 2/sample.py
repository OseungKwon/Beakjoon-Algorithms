def BTree(n, p):
    C=[[0 for x in range(n+1)] for y in range(n+1)]
    R = [[0 for x in range(n + 1)] for y in range(n + 1)]
    for i in range(1, n+1):
        C[i][i-1]=0
        C[i][i]=p[i]
        R[i][i]=i
    C[n+1][n]=0
    for diag in range(1, n):
        for j in range(1, n-diag+1):
            j=i+diag
            minval=99999

            for k in range(i,j+1):
                if(C[i][k-1]+C[k+1][j])<minval