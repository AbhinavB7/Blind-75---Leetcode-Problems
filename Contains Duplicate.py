class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort() #sort list in ascending order 
        n = len(nums)
        for i in range(1,n):
            if nums[i]==nums[i-1]: #compare adjacent elements 
                return True
        return False
