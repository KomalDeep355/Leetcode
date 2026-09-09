class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def findFirst():
            l = 0
            r = len(nums) - 1
            ans = -1

            while l <= r:
                m = (l + r) // 2

                if nums[m] == target:
                    ans = m
                    r = m - 1  # keep searching left
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            return ans

        def findLast():
            l = 0
            r = len(nums) - 1
            ans = -1

            while l <= r:
                m = (l + r) // 2

                if nums[m] == target:
                    ans = m
                    l = m + 1  # keep searching right
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1

            return ans

        return [findFirst(), findLast()]


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna