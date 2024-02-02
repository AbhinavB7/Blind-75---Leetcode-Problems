## 1 - Compare adjacent numbers after sorting
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort() #sort list in ascending order 
        n = len(nums)
        for i in range(1,n):
            if nums[i]==nums[i-1]: #compare adjacent elements 
                return True
        return False


## 2 - Compare every element with each other
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(0,n-1):
            for j in range(i+1, n):
                if nums[i]==nums[j]: #compare every element
                    return True
        return False
