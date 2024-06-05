class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert to lowercase
        s = s.lower()
        
        new = "" #creating a new string

        # if the character is alpha-numerical add to new
        for a in s:
            if a.isalnum():
                new += a
        
        # compare the string with its reverse
        if new == new[::-1]:
            return True
        else:
            return False 
