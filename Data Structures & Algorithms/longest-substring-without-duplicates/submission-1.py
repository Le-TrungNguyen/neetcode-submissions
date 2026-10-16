class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxres = 0
        subs = set()
        for end in range(len(s)):
            while s[end] in subs:
                subs.remove(s[start])
                start += 1
            subs.add(s[end])
            maxres = max(maxres, end - start + 1)
        return maxres