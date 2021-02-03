import sys
n=int(input())
check_Is=[0]*10001

for _ in range(n):
    num = int(sys.stdin.readline())
    check_Is[num]=check_Is[num]+1
for i in range(10001):
    if check_Is[i] != 0:
        for _ in range(check_Is[i]):
            print(i)