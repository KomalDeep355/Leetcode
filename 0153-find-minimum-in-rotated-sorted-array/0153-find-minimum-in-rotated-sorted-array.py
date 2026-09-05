class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            i = i % n
            nums[:]= nums[n-i:] +nums[:n-i]
            min_element= min (nums)
        return min_element

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna