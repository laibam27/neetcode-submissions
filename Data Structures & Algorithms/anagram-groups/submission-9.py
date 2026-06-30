class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a empty hashmap
        #loop thru list and add keys of different anagarms
        #check if anagram exists
        #if it does .append
        #if doesnt create new key
        #print

        group = {}

        for word in strs:
            key = tuple(sorted(word))
            if key in group:
                group[key].append(word)
            else:
                group[key] = [word]
        return list(group.values())
















        """


        group = {}

        for word in strs:
            key = tuple(sorted(word))
            if key in group:
                group[key].append(word)
            else:
                group[key] = [word]
        return list(group.values())
















        
        group = {}

        for word in strs:
            key = tuple(sorted(word))
            if key in group:
                group[key].append(word)
            else:
                group[key] = [word]
        return list(group.values())


        
        
        group = {} #empty hashmap

        for word in strs:
            key = tuple(sorted(word))
            if key in group:
                group[key].append(word)
            else:
                group[key] = [word]
        return list(group.values())
        
        """