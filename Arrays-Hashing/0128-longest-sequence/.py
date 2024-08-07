class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sets allow for O(1) look up

        numSet = set(nums)
        streak = 0

        for num in numSet:
            # check to get to the smallest number and then start from there
            if num - 1 not in numSet:
                curr = num
                curr_streak = 1
                
                # the while can at most run only O(n) times throughout the 
                # duration of the for loop due to O(1) look up
                while curr + 1 in numSet:
                    curr += 1
                    curr_streak += 1
                
                streak = max(streak, curr_streak)

        return streak
