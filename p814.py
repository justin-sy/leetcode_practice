# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node): # Traverse graph using DFS
            if not node: # If the node doesn't exist
                return True # Return True

            # Check if this part contains a one and shouldn't deleted
            delete = True
            if node.val == 1:
                delete = False
            
            # Travserse left and right and delete nodes
            if dfs(node.left):
                node.left = None
            if dfs(node.right):
                node.right = None

            # Return if should be deleted
            if not delete:
                return False
            return dfs(node.left) and dfs(node.right)
        
        # Traverse graph and see if root should be deleted
        if dfs(root):
            return None
        return root

