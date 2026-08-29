class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # return True if len(nums) != len(set(nums)) else False
        seen = set()
        for ele in nums:
            if ele in seen:
                return True
            else:
                seen.add(ele)
        return False
        