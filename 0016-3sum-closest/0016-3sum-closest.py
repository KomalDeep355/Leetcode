class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        n = len(nums)
        best_sum =best_sum = nums[0] + nums[1] + nums[2]

        for i in range(n):
            start = i + 1
            end = n - 1

            fixed = nums[i]

            while start < end:
                current_sum = fixed + nums[start] + nums[end]
                if abs(current_sum - target) < abs(best_sum - target):
                    best_sum = current_sum

                if current_sum < target:
                    start += 1

                elif current_sum > target:
                    end -= 1

                else:
                    return current_sum

        return best_sum

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna