from classes import *

def invertTree (root: Optional[TreeNode]) -> Optional[TreeNode]:
    #need to recursively turn all left nodes to right nodes
    

    #insert base case
    if root == None:
        return None
    left = root.left
    right = root.right
    root.right = invertTree(left)
    root.left = invertTree(right)
    return root


#passed, ok relatively easy