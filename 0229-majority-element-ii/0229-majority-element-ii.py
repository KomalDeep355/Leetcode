class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts={}
        for num in nums:
            counts[num] = counts.get(num, 0) + 1

            result=[]

        for num,freq in counts.items():
            if freq>len(nums)//3:
                result.append(num)
        return result

