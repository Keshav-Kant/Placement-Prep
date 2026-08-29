class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            adj = target - nums[i]
            if adj not in d:
                d[nums[i]] = i
            else:
                return [d[adj],i] 