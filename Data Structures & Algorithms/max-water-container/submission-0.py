class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = float("-inf")
        left = 0
        right = len(heights) - 1
        while left < right:
            curr_area = (right - left) * min(heights[right], heights[left])
            max_area = max(curr_area, max_area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area 