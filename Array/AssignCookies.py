# 455. Assign Cookies
class Solution:
    def findContentChildren(g: [int], s: [int]) -> int:
        kids = 0
        g.sort()  # O(n log n)
        s.sort()  # O(n log n)

        for c in s :    # check all cookies  O(n)
            if g[kids] <= c: # if the cookie can satisfy the child , then the kids +1 
                kids += 1
            if kids == len(g): # if all kids already get a cooides then break the loop.
                break
        print(kids)
        return kids

    g = [10,9,8,7]
    s = [5,6,7,8]
    findContentChildren(g, s)



'''
Summary : 
First it needs to sort the list by ordering .
use a two pointer to check all lists.
the kids as a index for checking g-list, it move only the previous kid who are satisfied.

time complexity : O(nlogn) + O(nlogn) + O(n) = O(ologn) 
space complexity :O(1) because only need  a space to save the kids variable.
'''