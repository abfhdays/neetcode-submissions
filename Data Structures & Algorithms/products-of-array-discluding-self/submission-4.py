class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodprefix = [0] * len(nums)
        prodprefix[0] = nums[0]

        for n in range(1, len(prodprefix)):
            prodprefix[n] = nums[n] * prodprefix[n-1]

        prodsuffix = [0] * len(nums)
        prodsuffix[-1] = nums[-1]

        for n in range(len(prodsuffix)-2, -1, -1):
            prodsuffix[n] = nums[n] * prodsuffix[n+1]

        res = [0] * len(nums)

        res[0] = prodsuffix[1]
        res[-1] = prodprefix[-2]

        for n in range(1, len(res)-1):
            res[n] = prodprefix[n-1] * prodsuffix[n+1]

        return res