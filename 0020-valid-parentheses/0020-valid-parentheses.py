class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs = {')': '(', ']': '[', '}': '{'}
        for i in range(len(s)):
            if s[i] in '({[' :
                stack.append(s[i])
            else :
                if not stack:
                    return False
                if stack[-1] == pairs[s[i]]:
                    stack.pop()
                else:
                    return False   
        return not stack     

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna