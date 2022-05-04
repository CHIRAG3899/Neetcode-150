#Given an array of strings strs, group the anagrams together. You can return the answer in any order.
#
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
# 
#
#Example 1:
#
#Input: strs = ["eat","tea","tan","ate","nat","bat"]
#Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#Example 2:
#
#Input: strs = [""]
#Output: [[""]]
#Example 3:
#
#Input: strs = ["a"]
#Output: [["a"]]

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if n <= 1:
            return [strs]
    
        strs_sorted = {}
        for i in range(n):
            s = ''.join(sorted(strs[i]))
            if s not in strs_sorted:
                strs_sorted[s] = [i]
            else:
                strs_sorted[s].append(i)
        
        res = []
        for key in strs_sorted:
            lst = []
            for i in strs_sorted[key]:
                lst.append(strs[i])
            res.append(lst)
            
        return res

class Solution:
    def groupAnagrams(self, strs):
        result = {}
        for s in strs:
            key = str(sorted(s))
            if key in result:
                result[key] += [s]
            else:
                result[key] = [s]
        return list(result.values())

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()