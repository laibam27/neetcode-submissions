class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create set that stores all nums
        #loop thru nums
        #if current num is in set -> return true
        #if current num is not in set -> add to set
        dupe = set()
        for num in nums:
            if(num in dupe):
                return True
            dupe.add(num)
        return False
        





















        """
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False






        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
"""
        
        