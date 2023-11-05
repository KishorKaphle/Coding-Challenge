#Sorting Ensemble
class sortingAlgo:
  def __init__(self) -> None:
    self.arr = arr

  def bubbleSort(self, arr):
   n = len(arr)
   for i in range(n):
     for j in range(0, n-i-1):
       if arr[j]>arr[j+1]:
        arr[j+1], arr[j] = arr[j], arr[j+1]
   return arr

  def selectionSort(self, arr):
   n = len(arr)
   for i in range(n):
     index_for_min = i
     for j in range(i+1, n):
       if arr[j]<arr[index_for_min]:
         index_for_min = j
         arr[i], arr[index_for_min] = arr[index_for_min], arr[i]
   return arr

  def insertionSort(self, arr):
   n = len(arr)
   for j in range(1, n):
     inserting_item_index = j
     while arr[j]<arr[j-1] and j >0:
       arr[j], arr[j-1] = arr[j-1], arr[j]
       j = j-1
   return arr

#example execution
arr = [3, 2, 6, 5, 7, 8, 3, 5, 1, 0, 9]
print(sortingAlgo().selectionSort(arr))