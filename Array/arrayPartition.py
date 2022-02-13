class Solution:
    def arrayPairSum(nums: [int]) -> int:
        
        # sort the array
        nums.sort() # O(nlogn)
        # base case -> only have a pair  
        if len(nums) == 2:
            return nums[0]
        ans = 0
        for i in range (0,len(nums),2): # O(n/2)
            ans += nums[i]
        return ans
    
    nums = [6,2,6,5,1,2]
    res = arrayPairSum(nums)
    print(res)
    
    # the time compexity is O(nlogn) + O(n/2) => O(nlogn)
    # the space comexity is O(n)
            