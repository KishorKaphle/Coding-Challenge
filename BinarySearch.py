#Binary Search Algorithms
def binarySrc(arr, high, low, key):
  mid = (high+low)//2
  
  if mid >0 and mid!=low:
   if arr[mid]==key: return mid
   elif arr[high]==key: return high
   elif arr[low]==key: return low
   elif arr[mid]>key: return binarySrc(arr, mid, low, key)
   elif arr[mid]<key: return binarySrc(arr, high, mid, key)
  
  else: 
    return ('Check provided key and list')


#Sample Execution
arr = [2, 2, 3, 4, 4,10, 10, 40, 50]
high = len(arr)-1
low = 0
#key = 0
#key = 100
key = 40
print(binarySrc(arr, high, low, key))