def matrix(arr1, arr2):
    result=[[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                result[i][j]+=(arr1[i][k]*arr2[k][j])
    return result
arr1=[[1, 4], [3, 2], [4, 1]]
arr2=[[3, 3], [3, 3]]
print(matrix(arr1,arr2))