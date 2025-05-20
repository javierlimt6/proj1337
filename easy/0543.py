from classes import *

def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    #for the diameter, its prob from the bottom left up to A root then back down all the way
    # so we need to keep track of 1. the max depth & 2. the max diameter of each side
    # so its smt like max(max_diameter(left), max_diameter(right), max_depth(left) + max_depth(right))
    # ill just update the nodes accordingly
    if root == None:
        return 0
    
    cur_max = max(self.diameterOfBinaryTree(root.left), self.diameterOfBinaryTree(root.right))
    
    if root.left:
        d_left = root.left.depth or 0
    else:
        d_left = 0
    if root.right:
        d_right = root.right.depth or 0
    else:
        d_right = 0
    
    root.depth = max(d_left, d_right) + 1


    return max(cur_max, d_left + d_right + 1)


#passed, took abit longer cause did not fully understand diameter, consider more of height than depth please thanks 

    