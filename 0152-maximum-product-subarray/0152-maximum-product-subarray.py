class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        max_product = nums[0]

        for i in range(1,len(nums)):
            num = nums[i]
            previous_max = current_max
            previous_min = current_min

            current_max = max(
                num,
                previous_max * num,
                previous_min * num
            )

            current_min = min(
                num,
                previous_max * num,
                previous_min * num
            )

            max_product = max(max_product, current_max)

        return max_product

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna