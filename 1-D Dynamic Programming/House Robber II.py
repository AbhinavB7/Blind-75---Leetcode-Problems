class Solution:
    def rob(self, nums: List[int]) -> int:
        num1 = 0
        num2 = 0
        num3 = 0
        num4 = 0

        if len(nums)==1:
            return nums[0]

        if len(nums)==0:
            return 0

        for n in range(1, len(nums)): 
            temp1 = num1
            num1 = max(num2+nums[n], num1)
            num2 = temp1
        
        for n in range(0, len(nums)-1):
            temp2 = num3
            num3 = max(num4+nums[n], num3)
            num4 = temp2

        return max(num1, num3)
