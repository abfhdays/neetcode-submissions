class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        if len(nums) == 3:
            return max(nums[1], nums[0] + nums[2])
        
        dp = [0] * (n)
        dp[0], dp[1], dp[2] = nums[0], nums[1], nums[0] + nums[2]
        # dp[2] = nums[2] + nums[0] = 10
        # dp[3] = nums[3] + max(nums[0], nums[1]) = 12
        # dp[4] = nums[4] + max(nums[1], nums[2])
        for i in range(3, n):
            dp[i] = nums[i] + max(dp[i-3], dp[i-2])
            print(dp[i])
        
        return max(dp[n-1], dp[n-2])