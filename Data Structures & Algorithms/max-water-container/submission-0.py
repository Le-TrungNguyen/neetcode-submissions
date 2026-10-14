class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1

        max_s = 0

        while left < right:
            h = min(heights[left], heights[right])
            w = right - left

            s = h*w

            if s > max_s:
                max_s = s
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_s