class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = {}

        for i in s:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1
        for i in t:
            if i in counts:
                counts[i] -= 1
            else:
                return False

        for i in counts.keys():
            if counts[i] != 0:

                return False
        
        return True