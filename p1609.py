# This solution uses BFS to solve problem 1609
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root]) # Queue to store nodes
        level = 0 # Current level
        while queue: # Run until all nodes have been visited
            prev = 0 # Previous node in level
            for i in range(len(queue)): # Iterate through all nodes in level
                node = queue.popleft() # Current node
                if level % 2 == node.val%2 or prev != 0 and level % 2 and node.val >= prev or not level % 2 and node.val <= prev: # Check if valid. First checks if should be even or odd. Then checks if it should be greater or less than previous node
                    return False # Return false if not valud
                prev = node.val # Set current node as previoous node for next cycle
                # Add the children of current node to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1 # Add one to level
        return True # Return true is every node is valid
            