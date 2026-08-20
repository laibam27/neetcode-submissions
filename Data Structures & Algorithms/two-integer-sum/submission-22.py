class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #start with a dictionary
        #..not set bc set will not store index
        #crete for loop for index and currentNum    
        #...looping thru nums
            #create var named diff = target-currentNum
            #if diff is in set
                #return [set[diff] , i]
            #else add currentNum to set
        allNums = {}
        for index, current_num in enumerate(nums):
            diff = target - current_num
            if diff in allNums:
                return [allNums[diff],index]
            allNums[current_num] = index



        ##########bad
        #make an empty array that holds the values of i and j
        #embeded loop - loops thru each number and \
        #finds the goal       number

        # second loop - loop through to see if the 
        #goal number is   ther
        #condion - index cannot be the same
        ###### bad
        """arr=[]

        left = 0
        right = len(nums)-1

        while(right>=left):
            sum = nums[left]+nums[right]
            if(target == sum):
                arr.append(left)
                arr.append(right)
                return arr
            elif target>sum:
                left+=1
            else:
                right-=1
        return arr"""
















"""
        arr = []

        for x in range (len(nums)):
            goal = target - nums[x]
            for y in range (len(nums)):
                if nums[y] == goal and x!=y: # first condion more niche
                    arr.append(x)
                    arr.append(y)
                    return arr



















        arr = []

        for num in range (len(nums)):
            goal = target-nums[num]

            for x in range (len(nums)):
                if nums[x] == goal and num != x:
                    arr.append(num)
                    arr.append(x)
                    return arr"""


        