# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from classes import *
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if p/q.left or right == false means dont match so propogate false
        if p == None or q == None:
            return p == q
        elif p.val != q.val:
            return False
        leftSame = Solution.isSameTree(p.left, q.left)
        rightSame = Solution.isSameTree(p.right, q.right)
        return leftSame and rightSame
        # check if p.left 


    #passed
    #quite easy, no issues here

