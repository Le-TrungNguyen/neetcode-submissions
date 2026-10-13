from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in nums]

        # Tạo map đếm số lượng từng số
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # Chia từ vào từng tần số
        for n, f in count.items():
            freq[f-1].append(n)
        
        # Duyệt từ tần số nhiều nhất
        res = []

        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res