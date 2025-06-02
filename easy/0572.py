# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from classes import *
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #use DFS, find candidates and perform isSameTree
        if root == None:
            return False
        if Solution.isSubtree(self, root.left, subRoot) or Solution.isSubtree(self, root.right, subRoot):
            return True
        if root.val == subRoot.val:
            return Solution.isSameTree(root, subRoot)
        return False

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #imported from 0100
        
        # if p/q.left or right == false means dont match so propogate false
        if p == None or q == None:
            return p == q
        elif p.val != q.val:
            return False
        leftSame = Solution.isSameTree(self, p.left, q.left)
        rightSame = Solution.isSameTree(self, p.right, q.right)
        return leftSame and rightSame
        

#PASSED
#straightforward DGS and checking 