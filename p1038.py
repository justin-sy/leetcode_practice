# DFS used to solve problem

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node,total): # DFS traversal
            if node.right: # traverse down the right side of the node and get those values
                total = dfs(node.right,total)
            total += node.val # add current node value to total greater values
            node.val = total # set current value equal to greater values
            if node.left: # traverse dow the left side of the node and add greater values
                total = dfs(node.left,total)
            return total # retrun greater values
        dfs(root,0)
        return root
            