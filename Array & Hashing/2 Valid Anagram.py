#Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
#An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
#
# 
#
#Example 1:
#
#Input: s = "anagram", t = "nagaram"
#Output: true
#Example 2:
#
#Input: s = "rat", t = "car"
#Output: false

class Solution:
    def isAnagram(self, s, t):
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:
            dic2[item] = dic2.get(item, 0) + 1
        return dic1 == dic2

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    
        if len(s) != len(t): # Check edge case for anagram
            return False
        # Time Complexity : O(n)
        # Space Complexity : O(26) , because a dictinary of max 26 characters can be created
        anagram = {}
        for i in range(len(s)):
            anagram[s[i]] = anagram.get(s[i],0) + 1
        
        for i in range(len(t)): 
            if t[i] in anagram:
                anagram[t[i]] = anagram.get(t[i],0) - 1
            else:
                return False
        for i in anagram:
            if anagram.get(i) !=0:
                return False
            else:
                return True
               
class Solution(object):
    def isAnagram(self, s, t):
        if(len(s)!=len(t)):
            return False
        r = Counter(s)
        m = Counter(t)
        
        for ele in r:
            if(r[ele]!=m[ele]):
                return False
        return True

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}
        
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True
