class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #create an empty array to store correct values
        #sort sums
        #create nested for loop, 
            #first for loop takes the first number
            #second for loop uses two pointers to get next two numbers
        #calculate threeSum to see if it is greater than or less than 0
        #if greater than 0, right pointer goes down
        #if less than 0, left pointer goes up

        arr = []
        nums.sort()

        for index, a in enumerate(nums):
            if index> 0 and a == nums[index-1]:
                continue
            left = index+1
            right = len(nums)-1
            while(right>left):
                threeSum = a + nums[left]+nums[right]
                if(threeSum == 0 ):
                    arr.append([a,nums[left],nums[right]])
                    left+=1
                    right-=1
                    while nums[left] == nums[left - 1] and left < right:
                         left += 1
        
    # Skip duplicates for right (looks forward to right + 1)
                    while nums[right] == nums[right + 1] and left < right:
                        right -= 1
                if(threeSum >0):
                    right-=1
                if(threeSum<0):
                    left+=1
        return arr
        




        