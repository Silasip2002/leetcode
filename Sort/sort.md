o# Sort 

## Quick Sort 
### theorem
 - first pick a x of array as a pivot 
 - you cna pick a x by different way such as first element , last element or random element...
 - do a checking if a value is smaller then the pivot then move to the left of x , if a value is bigger than x then move the value to the right.
 - using a recursive to do it until all the value have been sorted.
### code 
```
Pseudo Code for recursive QuickSort function :
quickSort(arr[],low,high){
    if (low < high) { 
        // keep doing until low = high
        
        pi = partition(arr,low,high); 

        quickSort(arr,low, pi -1) //before pi 
        quickSort(arr,pi+1, high) // After pi
    } 
}

// python 

def partition(arr,low,high):
    pivot = high
    pointer = low - 1

    for i in range (low, high):
        if arr[i] < arr[high]:
           ( arr[pointer + 1] arr[i]) = ( arr[i] arr[pointer + 1]) 
            pointer += 1
        
    (arr[pointer + 1],arr[pivot] ) = arr[pivot],arr[pointer + 1]
    return pointer + 1

def quickSort(arr:[int],low:int,high:int) -> int:
    if len(arr) <= 1:
        return arr
    
    if (low < high):
        pi = partition(arr,low,high)
        quickSort(arr,low, pi - 1)
        quickSort(arr,pi +1 , high)

// no return , because we are sorting in the same array
```
### time complexity
O(n^2) => each time the pivot is greatest or smallest value => each time sub-array  = (n-1) 
### space complexity
O(logn)


## Merge sort 
### theorem
### code 
### time complexity
### space complexity  


## Bubble sort 
### theorem
- loop all the len of arr
- using two for loop j , each time the len will be decrease by n - i - 1 
- because each time loop of i which means a biggest value has been sorted,
### code 
```
def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range( len(arr) - i - 1): // -i because each time the length will be reduce i , then -1 because the last one value do not need to be sort. 
            if arr[j+1] < arr[j]:
                arr[j+1],arr[j] = arr[j],arr[j+1]

return arr
```
### time complexity
 n * [n * 1 * 1] = O(n^2)
### space complexity  
O(n)
