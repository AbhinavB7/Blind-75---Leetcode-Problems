class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) # length of n
        
        sum_1 = 0
        sum_2 = 0

        for a in range(0, n+1):
            sum_1 += a
        
        for a in nums:
            sum_2 += a
            
        return sum_1 - sum_2
    
    
## 2 

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums) # length of n
        
        for a in range(0, n+1):
            if a not in nums: # check if a is present or not in nums
                return a

    