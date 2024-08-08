class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing stack problem
        # if the stack is greater than length of 1 then 
        # the stack is a non-strictly decreasing monotonic stack
        # indicating that the top of the stack should have the minimal
        # temperature 
        # -> checking only the top of the stack and then working backwards
        # ensures that checking the current temperature to previous ones
        # won't make unnecessary checks against previous ones since the 
        # smaller temperatures would have been checked already
        mono = [] # pair: [t, index]
        res = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            # while the current temp is greater than the top of stack temp
            while mono and t > mono[-1][0]:
                stackT, stackI = mono.pop()
                res[stackI] = i - stackI
            mono.append((t,i))
        return res

        # pushing and popping can each only occur n times throughout the 
        # algorithm -> bounded by O(n)
