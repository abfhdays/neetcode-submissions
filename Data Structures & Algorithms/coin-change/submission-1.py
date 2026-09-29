class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0]
        
        for n in range(1,amount+1):
            dp.append(-1)
        # coins = [1,2,5]
        #dp[0]=0
        #dp[1]=1
        #dp[2]=1
        #dp[3]=dp[1]+dp[2]
        #dp[4]=dp[2]+dp[2]
        #dp[5]=1
        #dp[6]=dp[5]+dp[1]=2
        #dp[7]=dp[5]+dp[2]=2
        #dp[8]=dp[6]+dp[2]=3
        #dp[9]=dp[7]+dp[2]=3
        #dp[10]=dp[5]+dp[5]=2
        #dp[11]=dp[10]+dp[1]=2
        #dp[12]=dp[10]+dp[2]=2
        # How do we choose the addition
        
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        print(dp)
        for n in range(1, amount+1):
            if dp[n] == 1:
                continue
            res = float('inf')
            for coin in coins:
                if n - coin > 0 and dp[n-coin] != -1:
                    res = min(res, 1 + dp[n-coin])
            if res != float('inf'):
                dp[n] = res
        
        print(dp)
        return dp[amount]
        