class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        freq = {0: 1}
        count = 0

        for num in nums:
            sum += num
            count += freq.get(sum - k, 0)
            freq[sum] = freq.get(sum, 0) + 1
        return count

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna