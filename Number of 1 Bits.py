class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        n = bin(n) # convert to binary

        for a in n: 
            if a == '1': 
                count += 1 # add 1 if the character is '1'
        return count 
        
        # while n != 0:    
        #     count += n % 2  # add 1 or 0 according to n
        #     n = n >> 1  # shift one to the right
        # return count
