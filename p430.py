"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        def dfs(prev,node):
            if node.child:
                temp = node.next
                node.next = node.child
                node.child.prev = node
                dfs(node,node.child)
                node.child = None
                while node.next:
                    node = node.next
                node.next = temp
                if temp:
                    temp.prev = node
            
            if node.next:
                dfs(node,node.next)

        dfs(None,head)
        return head