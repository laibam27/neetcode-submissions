class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for num in range (len(nums)):
            goal = target-nums[num]

            for x in range (len(nums)):
                if nums[x] == goal and num != x:
                    arr.append(num)
                    arr.append(x)
                    return arr

        
        