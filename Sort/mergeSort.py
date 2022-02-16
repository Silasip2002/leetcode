def mergeSort(arr):
    if len(arr) > 1:
        # set the pivot , and create two subArrays
        pivot = len(arr)//2   # // 2 return is a integer
        LsubArray = arr[:pivot]
        RsubArray = arr[pivot:]

        mergeSort(LsubArray)
        mergeSort(RsubArray)
        # set the 3 pointer 
        lPointer = rPointer = mainPointer = 0

        # compare two subarrays , smaller one should be assign to main array
        while lPointer < len(LsubArray) and rPointer < len(RsubArray):
            if LsubArray[lPointer] < RsubArray[rPointer]:
                arr[mainPointer] = LsubArray[lPointer]
                lPointer += 1
            else :
                arr[mainPointer] = RsubArray[rPointer]
                rPointer += 1
            mainPointer += 1

        # assign the reminder value to main array
        if lPointer < len( LsubArray):
            arr[mainPointer] = LsubArray[lPointer]
            lPointer += 1
            mainPointer += 1
        if rPointer < len(RsubArray):
            arr[mainPointer] = RsubArray[rPointer]
            rPointer += 1
            mainPointer += 1
        # call the mergeSort 


    print (arr)

                

        




array = [6, 5, 12, 10, 9, 1]

mergeSort(array)
