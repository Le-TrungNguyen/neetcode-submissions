class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            counts = [0] * 26

            for c in s:
                counts[ord(c) - ord('a')] += 1
            
            key = tuple(counts)
            if key not in hashmap:
                hashmap[key] = [s]
            
            else:
                hashmap[key].append(s)
        
        return list(hashmap.values())
