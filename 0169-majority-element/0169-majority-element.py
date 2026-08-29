class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
                h[i] +=1
        print(h)
        m = max(h)
        for key,value in h.items():
            if h[key] > h[m]:
                m = key

        return m
            
        