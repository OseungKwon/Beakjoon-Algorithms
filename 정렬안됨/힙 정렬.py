#힙 정렬
def heapify(arr, index, size):
    print("arr: ", arr)
    largest = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2
    if left_index < size and arr[left_index] > arr[largest]:
        largest = left_index
    if right_index < size and arr[right_index] > arr[largest]:
        largest = right_index
    if largest != index:
        arr[largest], arr[index] = arr[index], arr[largest]
        heapify(arr, largest, size)


def heap(arr):
    print("before max heap: ", arr)
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)
    return arr


n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
heap(arr)
