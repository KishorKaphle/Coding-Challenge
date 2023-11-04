#Selection Sorting
import matplotlib.pyplot as plt
import random
import numpy as np

def selectionSort(arr):
  n = len(arr)
  colors = np.random.rand(n)
  x = [ 1 for i in range(n)]

  for i in range(n):
    index_for_min = i
    for j in range(i+1, n):
      if arr[j]<arr[index_for_min]:
        index_for_min = j
    arr[i], arr[index_for_min] = arr[index_for_min], arr[i]
    plt.scatter(arr, x, s = [arr[i] for i in range(n)], c=colors, alpha = 0.5)
    plt.show()

  return arr

arr = [30, 150, 80, 300, 0, 100, 200, 400]
selectionSort(arr)