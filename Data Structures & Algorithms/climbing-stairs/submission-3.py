class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        # dp[0] = 0
        # dp[1] = 1
        # dp[2] = 2
        # dp[3] = 3
        # dp[4] = 5
        # dp[n] = dp[n-1] + dp[n-2] where dp[0] = 0, dp[1] = 1
        if n <= 2:
            return n
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]