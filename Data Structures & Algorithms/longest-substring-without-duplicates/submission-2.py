class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = defaultdict(int)
        longest = 0
        pointer = 0
        for i in range(len(s)):
            count[ord(s[i])] += 1
            while count[ord(s[i])] > 1:
                count[ord(s[pointer])] -= 1
                pointer += 1
                
            longest = max(longest, i - pointer + 1)
        return longest

