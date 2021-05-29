<<<<<<< HEAD
def heapify():
    for i in range(1, N):
        c = i
        while c > 0:
            root = (c - 1) // 2
            if numbers[c] > numbers[root]:
                numbers[c], numbers[root] = numbers[root], numbers[c]
            c = root
    return


# 힙 정렬하기(오름차순)
def heap_sort():
    for i in range(N - 1, -1, -1):  # n
        # 맨 앞과 맨 뒤를 교환! ( 가장 큰 수를 뒤로 보낸다. 그리고 그 가장 큰 수는 FIX!!!! )
        numbers[0], numbers[i] = numbers[i], numbers[0]

        # 힙구조가 이상해졌으므로 다시 힙구조로 바꾼다.  # logn
        root, c = 0, 1
        while c < i:
            c = root * 2 + 1
            if c < i - 1 and numbers[c] < numbers[c + 1]:
                c += 1

            if c < i and numbers[c] > numbers[root]:
                numbers[c], numbers[root] = numbers[root], numbers[c]
            root = c
    return


numbers = [1,8,6,5,3,7,4]
N = len(numbers)
heapify()
print(numbers)
heap_sort()
print(numbers)
=======
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
>>>>>>> b7ec4dcc454488091987978c0f608a8c0a2688d8
