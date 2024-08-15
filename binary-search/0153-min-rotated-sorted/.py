class Solution:
    def findMin(self, nums: List[int]) -> int:
        s, e = 0, len(nums) - 1
        curr = float("inf")
        while s < e:
            mid = s + ((e - s) // 2)
            curr = min(curr, nums[mid]) # take the min of the middle and current min
            if nums[mid] > nums[e]:
                s = mid + 1 # if mid is greater than the end, array is rotated -> the smallest number could only ever be to the right of the start if start is larger than the end
            else:
                e = mid - 1
        return min(curr, nums[s])