# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        index = 0
        head = TreeNode()
        dummy = head
        depths = [head]
        


        while index < len(traversal):
            number = ""
            cur_depth = 0

            while index < len(traversal) and traversal[index] != "-":
                number += traversal[index]
                index += 1

            dummy.val = int(number)

            if index  == len(traversal):
                return head

            while traversal[index] == "-":
                cur_depth += 1
                index += 1
            
                
            if cur_depth < len(depths):
                depths = depths[:cur_depth]
                dummy = depths[cur_depth-1]
                dummy.right = TreeNode()
                dummy = dummy.right
                depths.append(dummy)
            else:
                dummy.left = TreeNode()
                dummy = dummy.left
                depths.append(dummy)