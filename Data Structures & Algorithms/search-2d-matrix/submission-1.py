class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lrow, rrow = 0, len(matrix)-1

        while lrow < rrow:
            m = lrow + (rrow - lrow + 1) // 2
            if matrix[m][0] > target:
                rrow = m - 1
            else:
                lrow = m

        print(matrix[lrow])
        lcol, rcol = 0, len(matrix[0]) - 1

        while lcol < rcol:
            m = lcol + (rcol - lcol) // 2
            if matrix[lrow][m] > target:
                rcol = m - 1
            elif matrix[lrow][m] < target:
                lcol = m  + 1
            else:
                print(matrix[lrow][m])
                return True

        return matrix[lrow][lcol] == target 
