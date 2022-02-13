class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumOfLeftLeaves(root: [TreeNode]) -> int:
    sum = 0
    if root is None : return 0
    if(root.left and root.left.left is None and root.left.right is None):
        sum = root.left.val
    return sum + sumOfLeftLeaves(root.left) + sumOfLeftLeaves(root.right)
    

