class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = defaultdict(int)
        s2map = defaultdict(int)

        for l in s1:
            s1map[ord(l)] += 1

        starting_s2 = s2[:len(s1)]
        for l in starting_s2:
            s2map[ord(l)] += 1
        
        if s1map == s2map:
            return True

        for right in range(len(s1), len(s2)):
            s2map[ord(s2[right])] += 1
            left = ord(s2[right - len(s1)])
            s2map[left] -= 1
            if s2map[left] == 0:
                del s2map[left] 
            if s1map == s2map:
                return True

        return False

        