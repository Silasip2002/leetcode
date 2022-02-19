# Leetcode 56. Merge Intervals
class Solution:
    def merge(self, intervals):
        ans = []
        # sort the intervers base on a first value of interval
        sortedArr = sorted(intervals,key=lambda x:x[0])

        #check all the intervals 
        for interval in sortedArr:
            # if the arr is empty added the first interval into the ans or if the interval first value is larger than ans last value , that meas there is not overlap, also added the interval into the ans 
            if len(ans) <= 0 or interval[0] > ans[-1][1]:
                ans.append(interval)
            else:
                # if the interval[0] is smaller than last ans[-1][1] , that means there is a overlap, therefore , it needs to merge two arr. It is only need to replace the ans[-1][1] via interval[1]
                 ans[-1][1] = max(ans[-1][1],interval[1]) # using the max that because some case the first arr is coved the whole range of secondary array such [1,4] [2,3] that we also need to get the maximun value between ans[-1][0] and interval[1];
      
        print(ans)
        return ans



solution = Solution()
solution.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
