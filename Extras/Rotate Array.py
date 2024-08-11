class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        
        # reverse the whole array
        nums.reverse()

        # reverse the elements till k 
        rev_k = nums[:k]
        rev_k.reverse()
        nums[:k] = rev_k 

        # reverse remaining elements 
        rev_remaining = nums[k:]
        rev_remaining.reverse()
        nums[k:] = rev_remaining