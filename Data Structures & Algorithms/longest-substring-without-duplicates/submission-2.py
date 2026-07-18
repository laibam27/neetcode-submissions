class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #create a set that contains all of the letters
        #left =0
        #create a for loop that goes thru all of the chars in the string s
        #check is new char is already in the set
        #if it is in the set, remove the char anf everyhting before it
        #if it is not in the set, add it to the end of the set
        #return the size of the set


        charSet = set()
        max_length = 0
        left = 0
    

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left+=1
            charSet.add(s[right])
            new_length = right-left+1
            max_length = max(max_length , new_length)
        return max_length
        