class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        left = 1
        k = 1

        while left < n:
            if nums[left] != nums[left - 1]:
                nums[k] = nums[left]
                k += 1

            left += 1

        return k


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna