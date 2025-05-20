from classes import *

def maxDepth(self, root: Optional[TreeNode]) -> int:
    
    if root == None:
        return 0

    return max(maxDepth(root.left), maxDepth(root.right)) + 1
    

#passed, once again quite easy