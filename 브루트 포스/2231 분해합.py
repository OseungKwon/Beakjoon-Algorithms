n = int(input())
digit_n=list(map(int, str(n)))
def desum(n,digit_n):
    if(n>len(digit_n)*9):
        for i in range(n-len(digit_n)*9,n+1):
            digit = list(map(int, str(i)))
            if i+sum(digit)==n:
                return i
            if i==n:
                return 0
    else:
        for i in range(1,n+1):
            digit = list(map(int, str(i)))
            if i+sum(digit)==n:
                return i
            if i==n:
                return 0

print(desum(n,digit_n))