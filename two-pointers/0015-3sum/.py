class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # make each integer in the list the target and see if theres 
        # a two sum for that integer
        res = []
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + a == 0:
                    res.append([nums[l], nums[r], a])
                    l += 1
                    # have to keep moving the pointer to check for more solutions
                    # if you encounter a duplicate just keep moving the pointer
                    # while maintaining the rules
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif nums[l] + nums[r] + a > 0:
                    r -= 1
                elif nums[l] + nums[r] + a < 0:
                    l += 1
        return res


