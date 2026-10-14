class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        for i in s:
            countS[i] = countS.get(i, 0) + 1
        
        for i in t:
            if i not in countS:
                return False
            else:
                countS[i] -= 1
        
        for k, v in countS.items():
            if v != 0:
                return False

        return True