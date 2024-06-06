class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        sol = [] # empty set to store values
        for i in range(numRows):
            row = [1] * (i + 1) # creating the row with all 1's 
            for j in range(1, i):
                row[j] = sol[i - 1][j - 1] + sol[i - 1][j] # adding the two elements from the previous row
            sol.append(row)
        return sol

## j is the index of the element
# sol[i -1] is the previous row and j-1 and j represent the element just before the element in the current row and the current element in the current row
