def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    #dfs downwards, propogate if p or q found
    #if there is a node that has found both, immediately return that node
    def helper(node):
        # [p_found, q_found, value = None]
        if node == None:
            return [False, False, None]
        left = helper(node.left)
        right = helper(node.right)
        merged = [left[0] or right[0], left[1] or right[1], left[2] or right[2]]

        if node == p:
            merged[0] = True
        elif node == q:
            merged[1] = True
        if merged[0] and merged[1] and merged[2] == None:
            merged[2] = node
        
        return merged
    
    return helper(root)[2]