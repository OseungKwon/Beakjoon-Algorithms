while True:
    arr = list(map(int, input().split()))
    side=max(arr)
    if(sum(arr)==0):
        break
    arr.remove(side)
    if(arr[0]**2 + arr[1]**2 == side**2):
        print("right")
    else:
        print("wrong")