class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        for i in alpha:
            if s.count(i)!=t.count(i):
                return False
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna