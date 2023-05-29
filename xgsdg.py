def findSmallest(arr):
  smallest = arr[0]
  smallest_index = 0
  for i in range(1, len(arr0)):
    if arr[i] < smallest:
        smallest = arr[i]
        smallest_index = i
  return smallest_index

def selection_sort(arr):
    newarr=[]
    for i in range(len(arr)):
        smallest_index = findSmallest(arr)
        newarr.append(arr.pop(smallest_index))
    return newarr

arr0 = [4, 65, 2, -31, 0, 99, 83, 782, 1]

arr = selection_sort(arr0)

print(arr)