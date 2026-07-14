class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #create a empty list to store the values that add up to target
        #start left index on index 0
        #start right index on last index (len(range)-1)
        #calculate sum:
            #if sum is too large, make the right index go to the left by one: incr 1
            #if sum is too small, make the left index go to the right by one incr 1

        arr = []
        left = 0
        right = len(numbers)-1

        while(right>=left):
            sum = numbers[right]+ numbers[left]
            if(sum == target):
                arr.append(left+1)
                arr.append(right +1)
                return arr
            if(sum > target):
                right -=1
            if(sum<target):
                left+=1
        return arr

        