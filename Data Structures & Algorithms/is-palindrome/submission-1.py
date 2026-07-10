class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(" ", "")
        s = "".join(c for c in s if c.isalnum()).lower()
        left = 0
        right = len(s)-1
        while (left<=right):
            if(s[left].lower()==s[right].lower()):
                left+=1
                right-=1
            else:
                return False
        return True