#Linear Search
def linearSearch(arr, key):
  for i in range(len(arr)):
    if key ==arr[i]:
      index = i
      return index
      break
    
  
#Example Execution
arr = [1, 2, 5, 4, 7, 6, 8, 9, 4, 3, 7, 88, 7, 6, 4, 3, 2, 5, 8]
key = 88

print(linearSearch(arr, key))