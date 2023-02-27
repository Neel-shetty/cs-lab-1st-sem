# sorting and searching algorithms
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]

def linear_search(arr, k):
    n = len(arr)

    for i in range(n):
        if arr[i]==k:
            return i
        
def binary_search(arr,k, low, high):
    if high >= 1:
      mid = low + (high-1)//2

      if arr[mid]==k:
          return mid
      elif arr[mid]>k:
        return binary_search(arr,k,low,mid-1)
      else:
        return binary_search(arr,k,mid+1,high)
    else:
        return 'Element does not exist in the array'

        
        

arr = [ 2,5,79,0,15,4,8,9]
print('before sorting - {}'.format(arr))
print(linear_search(arr,15))
bubble_sort(arr)
print('after sorting - {}'.format(arr))
print(linear_search(arr,15))
print(binary_search(arr,15,0,len(arr)-1))
