class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        n = len(s)

        left = 0
        right = 0

        substring = set()
        longest = 0

        while right < n:

            if s[right] not in substring:
                substring.add(s[right])
                right += 1

                longest = max(longest, right - left)

            else:
                substring.remove(s[left])
                left += 1

        return longest

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna