def filter(n):
    if n<2:
        return False
    for i in range(2, n):
        if(n%i==0):
            return False
    return True

for i in range(int(input())+1):
    if(filter(i)):
        print(i)