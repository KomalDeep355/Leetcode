class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start = 0
        end = len(numbers)-1

        while start < end :
            crnt_two_sum = numbers[start]+ numbers[end]

            if  crnt_two_sum == target :
                return [start+1,end+1]
            elif crnt_two_sum > target:
                end-=1
            else:
                start+=1
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna