class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_s=''.join(char for char in s if char.isalnum())
        cleaned_s= cleaned_s.lower()
        return cleaned_s == cleaned_s[::-1]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna