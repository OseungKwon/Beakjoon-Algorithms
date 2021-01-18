# 경우의 수가 매우 많아서 유의해야 함
import math
T=int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2=map(int,input().split())
    distance=math.sqrt((abs(x1-x2)**2)+(abs(y1-y2)**2))
    if(x1==x2 and y1==y2):
        if(r1==r2):
            print(-1)
        else:
            print(0)
        continue
    if(distance==r1+r2 or r1==distance+r2 or r2==distance+r1):
        print(1)
    elif(distance>r1+r2 or r1>distance+r2 or r2>distance+r1):
        print(0)
    else:
        print(2)