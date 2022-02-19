# 75. Sort Colors

class Solution:
    def sortColors(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            for j in range(0, len(nums)-i-1):
                if (nums[j] > nums[j+1]):
                    nums[j+1],nums[j] = nums[j],nums[j+1]
        print (nums)
          
        

ans = Solution()
ans.sortColors([2,0,2,1,1,0])