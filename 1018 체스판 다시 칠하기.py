n, m=map(int, input().split())
arr=[]
for i in range(n):
    arr.append(input())
cnt=32
# 좌표탐색
for i in range(n-7):
    for j in range(m-7):

        # 홀수번째, 짝수번째 구분
        for odd in range(2):
            count=0

            # 지정된 좌표로 부터 +(0~8)까지 W,B의 참,거짓 판별
            for k in range(i,i+8):
                odd+=1
                for l in range(j,j+8):
                    if odd%2==0:
                        if arr[k][l]!='W':
                            count+=1
                    else:
                        if arr[k][l]!='B':
                            count+=1
                    odd += 1
            cnt=min(cnt,count)

print(cnt)