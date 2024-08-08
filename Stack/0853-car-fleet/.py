class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # sort the cars in order of postion
        # calculate the time the cars take to get to the goal
        # if a car behind the leading car gets to the target faster
        # then they form a fleet -> keep the lead car
        # b/c its slower
        cars = [[p, s] for p, s in zip(position, speed)]
        stack = []
        for p, s in sorted(cars)[::-1]: # start with the lead car
            stack.append((target-p)/s)
            if len(stack) > 1 and stack[-1] <= stack[-2]:
                stack.pop() # if the time of the car behind is less than the one in front pop the faster car
        return len(stack) # the length of the stack corresponds to the number of fleets
