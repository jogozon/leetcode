class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        curr = 0 
        count = 0
        # try to make the easiest solution possible
        while curr < len(arr):
            if arr[curr] % 2 == 1:
                curr += 1
                count += 1
                if count == 3:
                    return True
            else:
                count = 0
                curr += 1
        return False