class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_set = set(nums)
        longest_length = 0

        for num in num_set:
            if num - 1 not in num_set:
                current_length = 1

                while num + current_length in num_set:
                    current_length += 1

                longest_length = max(longest_length, current_length)

        return longest_length

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna