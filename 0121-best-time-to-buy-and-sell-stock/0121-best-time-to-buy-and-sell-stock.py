class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # global_max = 0

        # for i in range(len(prices)):
        #     for j in range(i+1,len(prices)):
        #         if prices[j] > prices[i]:
        #             local_max = 0
        #             n_a = prices[j:]
        #             n_a.sort()
        #             local_max = max(n_a[-1],local_max)
        #             global_max = max(global_max,local_max - prices[i]  )
        # return global_max
        global_max = 0
        global_max_profit = 0
        for i in range(len(prices)-1,-1,-1):
            global_max = max(global_max,prices[i])
            global_max_profit = max(global_max_profit,global_max - prices[i])
        return global_max_profit


            


        