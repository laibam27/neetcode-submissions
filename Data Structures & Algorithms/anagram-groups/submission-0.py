class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a empty hashmap
        #loop thru list and add different anagrams to different things
        #print

        groups = {}

        for word in strs:
            key = tuple(sorted(word))

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]
            
        return list(groups.values())
        
        