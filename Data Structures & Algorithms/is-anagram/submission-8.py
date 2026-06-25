class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        if sorted(s) == sorted(t):
            return True
        return False 























    
        if len(s) != len(t):
            return False
        
        arr1 = []
        arr2 = []

        for char in s:
            arr1.append(char)
        for char in t:
            arr2.append(char)
        
        arr1.sort()
        arr2.sort()

        if arr1 == arr2:
            return True
        return False






"""
        set1 = set()
        set2 = set()

        for num in s:
            set1.add(num)

        for num in t:
            set2.add(num)

        #set1 = sorted(set1)
        #set2 = sorted(set2)

        if set1 == set2:
            return True
        return False"""

