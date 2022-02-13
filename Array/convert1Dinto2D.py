class Solution:
    def construct2DArray(original: [int], m: int, n: int) -> [[int]]:
        
        col = 0 
        row = 0
        sizeOfInput = len(original)
        newMat = [[0 for i in range(n) ] for j in range(m)]

        if sizeOfInput != m*n: return [[]]
        
        for i in range(sizeOfInput):
            newMat[row][col] = original[i]
            col += 1
            if col == n:
                row += 1
                col = 0
        print(newMat)
        return newMat
        
    original = [1,1]
    m = 1
    n = 1
    res = construct2DArray(original,m,n)
    print("res" , res)

# 2022. Convert 1D Array Into 2D Array