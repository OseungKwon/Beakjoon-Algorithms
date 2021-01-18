while True:
    x=int(input())
    if(x==0):
        break
    count = 0
    arr = [True]*x

    for i in range(2, )
    for i in range(len(arr)):
        if (arr[i] != 0):
            for j in range(i + 1, len(arr)):
                if (arr[j] % arr[i] == 0):
                    arr[j] = 0
    for i in range(x+1,len(arr)):
        if(arr[i]!=0):
            count+=1

    print(count)

