
def partition(arr: [int], low: int, high: int):
 pivot = arr[high]
 pointer = low - 1

 # compare all the smaller value
 for i in range(low, high):
     if arr[i] < pivot:
         (arr[pointer + 1], arr[i]) = (arr[i], arr[pointer + 1])
         pointer += 1
# after comapre all the smaller value with pivot, then need to swap pivot
 (arr[pointer + 1] , arr[high]) =  (arr[high] , arr[pointer + 1])
 return pointer + 1

def quickSort(arr: [int], low: int, high: int) -> int:
   # base case 
   if len(arr) <= 1 :
       return arr
    
   # need to find the pivot if the low < high
   if low < high:
       pi = partition(arr,low,high)
       quickSort(arr,low,pi - 1)
       quickSort(arr,pi + 1, high)

    
data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted Array")
print(data)

size = len(data)

quickSort(data, 0, size - 1)

print('Sorted Array in Ascending Order:')
print(data)
