"""class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        for num in range (len(nums)):
            goal = target-nums[num]

            for x in range (len(nums)):
                if nums[x] == goal and num != x:
                    arr.append(num)
                    arr.append(x)
                    return arr

  """      
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
        