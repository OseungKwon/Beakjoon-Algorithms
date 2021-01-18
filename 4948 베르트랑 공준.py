def calc(x):
    count = 0
    m=int(x**0.5)
    arr = [True]*x

    for i in range(2, m+1):
        if(arr[i]==True):
            for j in range(i+i,x,i): #i*2부터는 False로
                arr[j]=False
    for i in range(2,x):
        if(arr[i]==True):
            count+=1
    return(count)

while True:
    x=int(input())
    if x==0:
        break
    if x==1:
        print(1)
    else:
        print(calc(x*2+1)-calc(x+1))



