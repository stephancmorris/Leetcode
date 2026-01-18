class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while matrix:
            res += (matrix.pop(0)) #adding the first row

            if matrix and matrix[0]: 
                for row in matrix: #loop through rows 
                    res.append(row.pop()) #add the last number of each row

            if matrix:
                res += (matrix.pop()[::-1]) #add in reverse order the last row

            if matrix and matrix[0]:

                for row in matrix[::-1]:
                    res.append(row.pop(0)) #move back up in the spiral / goes back to while loop

        return res
