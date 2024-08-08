class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        # this problem uses backtracking as its solution to exhaust
        # all permutations of the given parentheses that are acceptable


        def backtrack (openN, closedN, res):
            # basecase where the open and closed parentheses are maxxed
            if openN == closedN == n:
                res.append("".join(stack))
                return
            # if there are still open parentheses left to place
            # check to see if the following choices are valid

            # usually a for loop for the choices and then check if they are valid
            if openN < n:    
                stack.append("(")
                backtrack(openN + 1, closedN, res)
                # once the backtracking has exhausted the path here
                # we explore the previous decision that could have happened
                stack.pop()
            # if there are still closed parentheses to place
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1, res)
                stack.pop()

        backtrack(0, 0, res)
        return res