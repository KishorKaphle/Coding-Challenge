
def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j]>arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]

    return arr

arr = [0, 5, 2, 3, 1, 4]
print('Unsorted list: ', arr)
print('Sorted list: ', bubbleSort(arr))