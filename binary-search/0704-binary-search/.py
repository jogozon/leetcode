class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + ((r - l) // 2) # (l+r) // 2 leads to overflow - ie when the sum of l and r is greater than the maximum positive integer that can be stored in an int type variable
            if nums[m] > target:
                r = m - 1 # exclude the middle and take the left
            elif nums[m] < target:
                l = m + 1 # exclude the middle and take the right
            else:
                return m
        return -1