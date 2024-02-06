class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = sorted(s)
        t = sorted(t)
        if (s == t):
            return True
        return False
        # return (s == t)

# sorted(s) works for strings, it makes a new list, sort.(s) changes the existing list into ascending 
