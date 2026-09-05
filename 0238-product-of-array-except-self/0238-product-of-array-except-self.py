class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer=[1] * n
        left_product=1
        right_product=1
        for i in range(n):
            answer[i] = left_product
            left_product*= nums[i]
        for i in range (n-1,-1,-1):
            answer[i]*=right_product
            right_product*= nums[i]
        return answer


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna