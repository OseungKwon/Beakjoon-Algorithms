def optsearchtree(n, p):
    C = [[0 for x in range(0, n+1)] for y in range(0, n+2)]
    R = [[0 for x in range(0, n+1)] for y in range(0, n+2)]

    for i in range(1, n+1):
        C[i][i-1] = 0
        C[i][i] = p[i]
        R[i][i] = i
    C[n+1][n] = 0

    for diagonal in range(1, n):
        for i in range(1, n-diagonal+1):
            j = i + diagonal
            minval = 99999

            for k in range(i, j+1):
                if(C[i][k-1] + C[k+1][j]) < minval:
                    minval = C[i][k-1] + C[k+1][j]
                    kmin = k
            R[i][j] = kmin
            sum_ = p[i]
            for s in range(i+1, j+1):
                sum_ = sum_ + p[s]
            C[i][j] = minval + sum_
    return C[1][n], R
