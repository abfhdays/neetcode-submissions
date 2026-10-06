class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0

        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                mid = stack.pop()
                if not stack:
                    break
                res += ((min(height[stack[-1]], height[i])) - height[mid]) * (i - stack[-1] - 1)
            stack.append(i)
        return res
