class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=max_sum= nums[0]
        for n in nums[1:]:
            curr=max(n,curr+n)
            max_sum=max(max_sum,curr)
        return max_sum


        