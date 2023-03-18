#TC: O(len(arr) * len(str in array)) 
#SC: O(n)

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d={} # creating the dictionary 
        res = [] # creating the empty array
        for i in strs: # run until the value in strs
            key = sorted(i) # psorting and storing in key
            key = "".join(key) # sorting the key
            if key not in d: # if key not in d then add the ith value to dict
                d[key] = [str(i)]
            else:
                d[key].append(str(i)) # else append ith value to dict
        for k,v in d.items(): # looping the dictionary and appending the value to result
            res.append(v)
        return res # returning the result
