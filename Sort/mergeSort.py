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



def sortList(self, head):

    if head == None or head.next == None:
        return head
    
    mid = self.findmid(head)
    ri = mid.next
    mid.next = None
    mid = ri
    
    
    left = self.sortList(head)
    right = self.sortList(mid)
    
    return self.merge(left,right)

def findmid(self,head):
    fast = head.next
    slow = head
    
    while fast != None and fast.next != None:
        
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(self,list1,list2):
    new = ListNode()
    tail = new
    
    while list1 != None and list2 != None:
        if list1.val < list2.val :
            tail.next = list1
            tail = tail.next
            list1 = list1.next
        else:
            tail.next = list2
            tail = tail.next
            list2 = list2.next
            
    if list1 == None:
        tail.next = list2
    else:
        tail.next = list1
        
    new = new.next
    return new