class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash ={}
        for i , num in enumerate(nums):
            n = target - num
            if n not in hash:
                hash[num] = i
            else:
                return [hash[n],i]
