class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        MASK = 0xFFFFFFFF # mask to get last 32 bits
        MAX = 0x7FFFFFFF # maximum value for a 32-bit integer

        while b != 0:
            
            carry = (a & b) << 1 & MASK # AND and shift 1 to left within the mask range
            a = (a ^ b) & MASK # XOR also within mask range
            b = carry

        return a if a <= MAX else ~(a ^ MASK)
