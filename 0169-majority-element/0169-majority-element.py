class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts={}
        for num in nums:
             counts[num] = counts.get(num, 0) + 1
             if counts[num] > len(nums) // 2:
                return num
                 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna