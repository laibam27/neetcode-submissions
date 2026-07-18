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
        max_len = 0
        left = 0

        for right in range(len(s)):
            while s[right] in charSet:
                charSet.remove(s[left])
                left +=1
            new_len = right-left+1
            max_len = max(max_len,new_len)
            charSet.add(s[right])
        return max_len
        