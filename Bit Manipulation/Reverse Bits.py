class Solution:
    def reverseBits(self, n: int) -> int:
        n = bin(n)[2:] # integer to a binary string, remove the '0b' prefix
        n = n.zfill(32) # Pad the binary string to ensure it is 32 bits
        
        rev_n = n[::-1] # Reverse
        rev_int = int(rev_n, 2) # binary to integer
        
        return rev_int
        