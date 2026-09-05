class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n =len(nums)
        result =[]
        seen=set (nums)
        for i  in range(1,n+1):
            if i not in seen:
                result.append(i)
            else:
                continue
        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna