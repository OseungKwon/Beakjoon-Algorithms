## 기수 정렬
def counting_sort(arr, digit):
    n=len(arr)
    output=[0]*(n)
    count=[0]*(10)

    for i in range(0, n):
        index = int(arr[i]/digit)
        count[ (index)%10 ] += 1

    for i in range(1,10):
        count[i] += count[i-1]
    print(count)
    i=n-1
    while i>=0:
        index = int(arr[i]/digit)
        output[count[(index)%10]-1]=arr[i]
        count[(index)%10]-=1
        i-=1
    print(count)
    print('output', output)
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    maxValue = max(arr)
    digit = 1
    while int(maxValue/digit)>0:
        counting_sort(arr,digit)
        digit *=10

arr = [170, 45, 75, 90, 802, 24, 2, 66]
radix_sort(arr)

for i in range(len(arr)):
    print(arr[i], end=" ")
