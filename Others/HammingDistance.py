from array import array


class Solution:
    def hammingDistance(x:int,y:int) -> int:
        return bin(x^y).count("1")



    # input test
    x = 1
    y = 8
    ans = hammingDistance(x,y)
    print(ans)


            
