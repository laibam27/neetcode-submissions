class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        #cerate expected by sorting heights in order
        #go thru array to find if it is increasing
        #if num i-1 > i output heights[i-1]
        expected = sorted(heights)
        index = 0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                index += 1
        return index
