class Solution:
    def matrixReshape(mat: [[int]], r: int, c: int) -> [[int]]:
       
        # doing some base case 
        sizeOfRow = len(mat) 
        sizeOfCol = len(mat[0])
        if mat is None : return mat  
        if sizeOfRow * sizeOfCol != r * c : return mat
        
        # moethod 1
        # # create a empty martrix
        # ans = [[0 for i in range(c)] for j in range(r)]  # fist assign the zero value into the size of col which returns an array. them we will assign this array into size of row which will finally returns a martrix
        # for i in range(0, sizeOfRow * sizeOfCol) :    #O(n*m) * O(1).... = O(n*m)
        #     org_y = int(i / sizeOfCol)
        #     org_x = int(i % sizeOfCol)
        #     new_y = int(i / c)
        #     new_x = int(i % c)
        #     print("org",org_y,org_x)
        #     print("new",new_y,new_x)
        #     ans[new_y][new_x] = mat[org_y][org_x] 
        #     # using the ans for spacing which need to n * m size , therefore, the space compexity is O(n*m)
        # print("ans", ans)
        # return ans

        # Method 2
        # set up two pointers 
        col = 0 
        row = 0
        ans = [[0 for i in range(c)] for j in range(r)]
        for i in range(sizeOfRow):
            for j in range(sizeOfCol):
                ans[row][col] = mat[i][j]
                col += 1
                if col == c:
                    row += 1
                    col = 0
        print(ans)

    # example input
    mat = [[1,2],[3,4]]
    # init martrix [[0], [0], [0], [0]]
    r = 4
    c = 1
    matrixReshape(mat,r,c)
            
                    
                
                
        
        
                
       
        
        