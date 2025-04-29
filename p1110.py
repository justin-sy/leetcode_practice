# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root: # If there is no root
            return []
        to_delete = set(to_delete) # Convert to set
        Hashmap = {root.val:root} # Hashmap to store roots
        def dfs(node): # Use DFS to traverse the graph
            delete = False # Variable for whether or not to delete the node
            if node.val in to_delete: # If the node should be deleted
                if node.val in Hashmap: # If the node is a root
                    Hashmap.pop(node.val) # Remove the root
                if node.left: # If the left child  exists
                    Hashmap[node.left.val] = node.left # Add left child as new root
                if node.right: # If the right child  exists
                    Hashmap[node.right.val] = node.right # Add right child as new root
                delete = True # Delete the node
            if node.left and dfs(node.left): # If there is a left child and should be deleted
                node.left = None # Delete left child
            if node.right and dfs(node.right): # If there is a right child and should be deleted
                node.right = None # Delete right child
            return delete # Retunr if node should be deleted
        dfs(root) # Traverse the graph
        return list(Hashmap.values()) # Return the roots