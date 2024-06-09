class Solution:
    def rob(self, nums: List[int]) -> int:
        num1 = 0
        num2 = 0
        
        for n in nums:
            temp = num1
            num1 = max(num2+n, num1)
            num2 = temp
        return num1
            