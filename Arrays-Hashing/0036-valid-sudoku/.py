class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        res = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element != '.':
                    # each element in the row and the column should be unique
                    # each element in 9 grid sections shoul be unique also
                    res += [(i, element), (element, j), (i // 3, j // 3, element)]
        # checks to make sure that the length of the results is the same as the unique 
        # set
        return len(res) == len(set(res))