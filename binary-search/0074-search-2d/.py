class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # just run two binary searchs, one on the rows and one on the array
        top, bottom = 0, len(matrix) - 1
        m = 0
        while top <= bottom:
            m = ((top+bottom) // 2)
            if target > matrix[m][-1]:
                top = m + 1
            elif target < matrix[m][0]:
                bottom = m - 1
            else:
                break
        l, r = 0, len(matrix[0]) - 1
        if not(top <= bottom):
            return False
        while l <= r:
            mid = ((r+l) // 2)
            if target > matrix[m][mid]:
                l = mid + 1
            elif target < matrix[m][mid]:
                r = mid - 1
            else:
                return True
        return False

        