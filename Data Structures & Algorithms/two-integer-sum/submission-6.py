class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #make an empty array that holds the values of i and j
        #embeded loop - loops thru each number and finds the goal number
        # second loop - loop through to see if the goal number is ther
        #condion - index cannot be the same
         
        arr = []

        for x in range (len(nums)):
            goal = target - nums[x]
            for y in range (len(nums)):
                if nums[y] == goal and x!=y:
                    arr.append(x)
                    arr.append(y)
                    return arr



















        """arr = []

        for num in range (len(nums)):
            goal = target-nums[num]

            for x in range (len(nums)):
                if nums[x] == goal and num != x:
                    arr.append(num)
                    arr.append(x)
                    return arr"""


        