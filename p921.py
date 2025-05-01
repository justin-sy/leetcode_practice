# This solution utilizes a stack to solve the problem
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = [] # Stack to store parentheses
        for x in s: # Iterate through the string of parentheses
            if x == ")": # Check if closing parentheses
                if stack and stack[-1] == "(": # Remove last open parentheses if present
                    stack.pop()
                else: # Add to stack if close is not last in stack
                    stack.append(")")
            else: # Add openening parentheses to stack
                stack.append("(")
        return len(stack) # Return length of stack