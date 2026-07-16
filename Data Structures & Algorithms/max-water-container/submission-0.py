class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #create left and right pointer
        #create a variable that stores the largest amount
        #create a while loop for the first num in the array
        #imbeded in the while loop have the right pointer go through eveyrthing to find max
        
        largest = 0
        left = 0
        right = len(heights)-1
        while(left<right):
            lower = min(heights[left], heights[right])
            current_area = (right-left)*lower
            largest = max(largest, current_area)
            if(heights[left]<heights[right]):
                left+=1
            else:
                right-=1
        return largest
            
        