from ast import List

class Solution:
    def removeElement(nums: [int], val: int) -> int:
        pointer = 0 
        for i in range (len(nums)):
            if nums[i] != val :
                nums[pointer] = nums[i]
                pointer += 1
        print ("pointer ", pointer)
        print ('modified nums', nums)
        return pointer 

    nums = [0,1,2,2,3,0,4,2]
    removeElement(nums,2)




     

