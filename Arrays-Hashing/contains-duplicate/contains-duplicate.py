class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #  nums.sort()
        #  for i in range(len(nums) - 1):
        #     if nums[i] == nums[i+1]:
        #         return True
        #  return False

# time complexity: O(nlogn) assuming sort works like that
# space complexity: O(n)

        hashSet = set()
        for n in nums: 
            if n in hashSet:
                return True
            else:
                hashSet.add(n)
        return False

# time complexity: O(n)
# space complexity: O(n)
            