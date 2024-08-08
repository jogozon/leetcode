class Solution:
    def res(self, x: int, y: int, op: str) -> int:
        if op == "+":
            return y + x
        elif op == "-":
            return y - x
        elif op == "/":
            return int (y / x)
        elif op == "*":
            return y * x
        return 0

    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        ops = "+-*/"
        for token in tokens:
            if token not in ops:
                nums.append(int(token))
            else:
                # the idea here that the operator only applies to the two values 
                # that occur before it and they can happen in any order
                # -> calculate the values when the operator occurs 
                x = nums[-1]
                y = nums[-2]
                nums[-2] = self.res(x, y, token)
                nums.pop()
        return nums[0]
                