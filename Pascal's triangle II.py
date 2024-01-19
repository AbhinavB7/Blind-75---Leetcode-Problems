class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Create a 2D list to represent Pascal's Triangle up to rowIndex + 1
        tria = [[] for _ in range(rowIndex + 1)]
        
        colNum = 1  # Initialize column number
        
        # Iterate through each row up to rowIndex
        for r in range(rowIndex + 1):
            row = [1] * colNum  # Initialize a new row with all elements as 1
            tria[r] = row  # Update the current row in the triangle
            
            # Update the elements in the current row (excluding the first and last)
            for c in range(1, colNum - 1):
                tria[r][c] = tria[r - 1][c - 1] + tria[r - 1][c]  # Calculate the value based on the values in the row above
            
            colNum += 1  # Increment column number for the next row
        
        return tria[rowIndex]  # Return the row at the specified index
