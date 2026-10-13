class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        prefix = 1
        # Prefix: tính tích các phần tử trước phần tử đang xét
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
        
        # Postfix: tính tích các phần tử sau phần tử đang xét
        postfix = 1
        for i in range(n-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res