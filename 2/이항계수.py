def bin(n,k):
    B = [[0] * (k + 1) for _ in range(n + 1)]
    for i in range(n+1):
        for j in range(min(i,k)+1):
            if j==0 or j==i:
                B[i][j]=1
            else:
                B[i][j]=B[i-1][j]+B[i-1][j-1]
    return B[n][k]

print(bin(5,2))
