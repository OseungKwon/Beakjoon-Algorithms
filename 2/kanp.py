N, W = 4, 5
w = [2, 1,3,2]
b = [12,10,20,15]

knap = [[0 for _ in range(W+1)] for _ in range(N+1)]

for i in range(N+1):
    for j in range(W+1):
        if i==0 or j==0:
            knap[i][j]=0
        elif w[i-1] <= j:
            knap[i][j] = max(b[i-1] + knap[i-1][j-w[i-1]],  knap[i-1][j])
        else:
            knap[i][j] = knap[i-1][j]

print(knap)