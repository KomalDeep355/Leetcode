class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        n = len(nums)
        result = set()

        for i in range(n):
            start = i + 1
            end = n - 1

            target = -nums[i]

            while start < end:
                current_two_sum = nums[start] + nums[end]

                if current_two_sum == target:
                    result.add((nums[i], nums[start], nums[end]))

                    start += 1
                    end -= 1

                elif current_two_sum > target:
                    end -= 1

                else:
                    start += 1

        return [list(triplet) for triplet in result]

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna