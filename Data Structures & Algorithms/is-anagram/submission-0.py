class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterss=list(s)
        letterst=list(t)
        
        
        if sorted(letterss) == sorted(letterst):
            return True 

        else:
            return False
            