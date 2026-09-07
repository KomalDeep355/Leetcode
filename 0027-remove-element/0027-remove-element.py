class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)

        if n == 0:
            return 0

        left = 0
        k = 0

        while left < n:
            if nums[left] != val:
                nums[k] = nums[left]
                k += 1

            left += 1

        return k

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna