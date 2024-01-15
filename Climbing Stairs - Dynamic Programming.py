class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        a = 1
        b = 2
        x = 0

        for i in range(2, n):
            x = a + b
            a = b
            b = x
        return x




