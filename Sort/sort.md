# Sort 

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



```
### time complexity
### space complexity  

## Merge sort 
### theorem
### code 
### time complexity
### space complexity  