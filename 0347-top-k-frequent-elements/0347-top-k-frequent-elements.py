class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result=[]
        freq=[]
        for i in range(len(nums)):
            if nums[i] in result:
                continue
            count = nums.count(nums[i])
            result.append(nums[i])
            freq.append(count)
        answer =[]
        for j in range(k):
            max_freq=max(freq)
            index = freq.index (max_freq)
            answer.append(result[index])
            freq[index]=-1
        return answer
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna