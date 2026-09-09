class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        n = len(nums)
        r = n - 1
        
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
    
            if nums[l] <= nums[m]:  # left half is sorted
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1

            else:  # right half is sorted
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna