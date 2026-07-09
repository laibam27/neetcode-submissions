class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #create empty list to store output list
        #create a for loop to loop thru nums

        output = []
        for x in range(len(nums)):
            out = 1
            for y in range(len(nums)):
                if x == y:
                    continue
                else:
                    out *= nums[y]
            output.append(out)
        return output