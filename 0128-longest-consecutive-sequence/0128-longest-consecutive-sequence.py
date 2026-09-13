class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()

        current_length = 1
        longest_length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                current_length += 1

            elif nums[i] == nums[i - 1]:
                continue

            else:
                current_length = 1

            longest_length = max(longest_length, current_length)

        return longest_length

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna