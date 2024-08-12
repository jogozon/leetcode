class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # approach from both ends of the list and then update by the min height
        l, r = 0, len(heights) - 1
        maxH = 0
        while l < r:
            maxH = max(maxH,min(heights[l], heights[r]) * (r - l))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxH
