class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        freq={}
        for i in range (n):
            comp=target - numbers[i]
            if comp in freq:
                return [freq[comp]+1 , i+1]
            freq [numbers[i]]=i


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna