#카운팅 정렬
def counting(array, max):
    count_arr = [0] * (max + 1)

    for i in array:
        count_arr[i] += 1
        print(count_arr[i])
    for i in range(max):
        count_arr[i + 1] += count_arr[i]
    output_arr = [-1] * len(array)

    for i in array:
        output_arr[count_arr[i] - 1] = i
        count_arr[i] -= 1
    return output_arr


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

max = arr[0]
for i in range(len(arr)):
    if arr[i] > max:
        max = arr[i]
print(counting(arr, max))
