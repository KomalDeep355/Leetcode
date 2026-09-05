class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        for i  in range (n+1):
            if i in nums:
                continue
            else:
                return i

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna