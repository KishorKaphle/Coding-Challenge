#Insertion Sort Algo

def insertionSort(arr):
  n = len(arr)
  for j in range(1, n):
    inserting_item_index = j
    while arr[j]<arr[j-1] and j >0:
      arr[j], arr[j-1] = arr[j-1], arr[j]
      j = j-1
  
  return arr

arr = [1, 4, 5, 2, 7, 4, 8 ,9, 0]
print('unsorted list: ', arr)
print('sorted list: ', insertionSort(arr))