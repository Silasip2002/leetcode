from functools import cmp_to_key
from tokenize import String
class Solution:
    def largestNumber(self, nums:[int]) -> str:

        # create a compere function 
        def cmp_func(x:[String], y:[String]):
            if x + y > y + x:
                return 1
            elif x == y:
                return 0
            else:
                return -1

        nums = [str(num) for num in nums] # convet all the value into String

        # sorted the string base on the custom compare function
        res = sorted(nums, key = cmp_to_key(cmp_func),reverse=True) 
        print(res)
        #join all the value into a string and remove the first 0 in the string. lstrip -> to move all left side 0 value. but it wil return 0 in "00" is situation. therefore, if it return empty then we just return 0 instend
        print(''.join(res).lstrip('0') or "0")
solution = Solution()
solution.largestNumber([3, 30, 34, 5, 9])
