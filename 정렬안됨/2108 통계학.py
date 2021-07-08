import sys
from collections import Counter

n = int(sys.stdin.readline())
check_Is = [0] * 8002
count=0

sum = 0

mid = 0

max = 0
min = 8002


for _ in range(n):
    num = int(sys.stdin.readline())
    check_Is[num + 4001] = check_Is[num + 4001] + 1
nums_s = Counter(check_Is).most_common()
#print('nums_s',nums_s)
for i in range(8002):
    if check_Is[i] != 0:
        for j in range(check_Is[i]):
            sum += i

            if count == n // 2:
                mid = i
            if max<i:
                max=i
            if min>i:
                min=i
            count += 1
print(sum // n - 4001)
print(mid-4001)
print("최빈값 자리")
print(max-min)