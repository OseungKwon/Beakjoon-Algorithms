def matrix_multiplication(mat1, mat2):
    matR = [len(mat2[0]) * [0] for i in range(len(mat1))]
    count=0
    for i in range(len(matR)):
        for j in range(len(matR[i])):
            for k in range(len(mat1[i])):
                matR[i][j] += mat1[i][k] * mat2[k][j]
                count+=1

    return matR,count

mat1=[[2,2,2,2],[2,2,2,2],[2,2,2,2],[2,2,2,2]]
mat2=[[1,1,1,1],[1,1,1,1],[1,1,1,1],[1,1,1,1]]
print(matrix_multiplication(mat1,mat2))