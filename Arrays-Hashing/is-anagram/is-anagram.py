class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
    
        # sort each string and check if they are equal
        # time: O(nlogn)
        # space: O(1)

        if len(s) != len(t):
            return False
        countS = {}
        countT = {}

        for i in range(len(s)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
            countS[s[i]] = 1 + countS.get(s[i], 0)
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        return True

        # time: O(n)
        # space: O(n)
            