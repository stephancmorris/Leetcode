class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        CheckForClosing = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in CheckForClosing:
                #Check the stack
                if stack and stack[-1] == CheckForClosing[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if not stack:
            return True
        else: 
            return False